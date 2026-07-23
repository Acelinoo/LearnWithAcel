"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { AlertCircle, RefreshCw, X } from "lucide-react";

export default function ErrorToast({ message = "Gagal menghubungkan ke server." }) {
  const router = useRouter();
  const [isVisible, setIsVisible] = useState(true);
  const [isRetrying, setIsRetrying] = useState(false);

  useEffect(() => {
    setIsVisible(true);
  }, [message]);

  const handleRetry = () => {
    setIsRetrying(true);
    // Triggers a server component re-fetch without full page reload
    router.refresh();
    
    // Optional: Reset retry state after a short delay
    setTimeout(() => {
      setIsRetrying(false);
    }, 1000);
  };

  if (!isVisible) return null;

  return (
    <div className="fixed bottom-6 right-6 z-50 flex max-w-sm animate-in slide-in-from-bottom-5 items-center gap-3 rounded-lg border border-red-500/20 bg-red-500/10 p-4 text-sm text-red-200 shadow-glow backdrop-blur-md">
      <AlertCircle size={18} className="text-red-400 shrink-0" />
      <span className="flex-1">{message}</span>
      
      <button 
        onClick={handleRetry}
        disabled={isRetrying}
        className="flex items-center gap-1.5 rounded bg-red-500/20 px-2 py-1 text-xs font-medium text-red-300 transition-colors hover:bg-red-500/30 disabled:opacity-50"
      >
        <RefreshCw size={12} className={isRetrying ? "animate-spin" : ""} />
        Coba Lagi
      </button>

      <button 
        onClick={() => setIsVisible(false)}
        className="ml-2 text-red-400/70 hover:text-red-400 transition-colors"
      >
        <X size={16} />
      </button>
    </div>
  );
}
