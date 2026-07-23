"use client";

import { useState, useEffect } from "react";
import { Search, Shield, ShieldOff, Check, AlertCircle } from "lucide-react";
import { listAdminUsers, updateUserRole, type UserSummary } from "@/lib/api/admin";
import { toast } from "sonner";
import { cn } from "@/lib/utils";
import AdminDeleteModal from "./AdminDeleteModal";

type Props = {
  token: string;
};

export default function UserManager({ token }: Props) {
  const [users, setUsers] = useState<UserSummary[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [search, setSearch] = useState("");
  const [targetUser, setTargetUser] = useState<UserSummary | null>(null);

  const fetchUsers = async () => {
    setIsLoading(true);
    try {
      const res = await listAdminUsers(token);
      setUsers(res.users);
    } catch (err) {
      toast.error("Gagal mengambil data user");
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchUsers();
  }, [token]);

  const filteredUsers = users.filter((u) => {
    const s = search.toLowerCase();
    return u.email.toLowerCase().includes(s) || u.full_name.toLowerCase().includes(s);
  });

  const handleRoleToggle = async () => {
    if (!targetUser) return;
    const newRole = !targetUser.is_admin;
    try {
      await updateUserRole(targetUser.id, newRole, token);
      toast.success(`Berhasil mengubah role ${targetUser.full_name}`);
      fetchUsers();
    } catch (err) {
      toast.error("Gagal mengubah role user");
      console.error(err);
    } finally {
      setTargetUser(null);
    }
  };

  return (
    <div className="space-y-6">
      <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
        <h2 className="font-display text-xl font-semibold">Daftar Pengguna</h2>
        <div className="relative">
          <Search size={16} className="absolute left-3 top-1/2 -translate-y-1/2 text-muted" />
          <input
            type="text"
            placeholder="Cari email atau nama..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="h-10 w-full rounded-xl border border-border bg-black/40 pl-10 pr-4 text-sm placeholder:text-muted focus:border-accent focus:outline-none focus:ring-1 focus:ring-accent sm:w-64"
          />
        </div>
      </div>

      <div className="overflow-hidden rounded-xl border border-border">
        <table className="w-full text-left text-sm">
          <thead className="bg-black/40 text-muted">
            <tr>
              <th className="px-4 py-3 font-medium">Nama</th>
              <th className="px-4 py-3 font-medium">Email</th>
              <th className="px-4 py-3 font-medium">Status Role</th>
              <th className="px-4 py-3 font-medium text-right">Aksi</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-border">
            {isLoading ? (
              <tr>
                <td colSpan={4} className="p-8 text-center text-muted">
                  Memuat data pengguna...
                </td>
              </tr>
            ) : filteredUsers.length === 0 ? (
              <tr>
                <td colSpan={4} className="p-8 text-center text-muted">
                  Tidak ada pengguna ditemukan.
                </td>
              </tr>
            ) : (
              filteredUsers.map((user) => (
                <tr key={user.id} className="transition-colors hover:bg-black/20">
                  <td className="px-4 py-3 font-medium">{user.full_name}</td>
                  <td className="px-4 py-3 text-muted">{user.email}</td>
                  <td className="px-4 py-3">
                    <span
                      className={cn(
                        "inline-flex items-center gap-1 rounded-full px-2 py-0.5 text-[11px] font-medium uppercase tracking-wide",
                        user.is_admin
                          ? "bg-accent/20 text-accent"
                          : "bg-border text-muted-foreground"
                      )}
                    >
                      {user.is_admin ? (
                        <>
                          <Shield size={10} /> Admin
                        </>
                      ) : (
                        <>
                          <Check size={10} /> Student
                        </>
                      )}
                    </span>
                  </td>
                  <td className="px-4 py-3 text-right">
                    <button
                      onClick={() => setTargetUser(user)}
                      className={cn(
                        "inline-flex items-center gap-1.5 rounded-lg px-3 py-1.5 text-xs font-medium transition-colors",
                        user.is_admin
                          ? "bg-red-500/10 text-red-500 hover:bg-red-500/20"
                          : "bg-accent/10 text-accent hover:bg-accent/20"
                      )}
                    >
                      {user.is_admin ? (
                        <>
                          <ShieldOff size={14} /> Cabut Admin
                        </>
                      ) : (
                        <>
                          <Shield size={14} /> Jadikan Admin
                        </>
                      )}
                    </button>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>

      <AdminDeleteModal
        isOpen={!!targetUser}
        title={`Ubah Role: ${targetUser?.full_name}`}
        description={`Apakah Anda yakin ingin mengubah status pengguna ini menjadi ${targetUser?.is_admin ? "STUDENT" : "ADMIN"}?`}
        onConfirm={handleRoleToggle}
        onCancel={() => setTargetUser(null)}
        confirmText="Ubah Role"
      />
    </div>
  );
}
