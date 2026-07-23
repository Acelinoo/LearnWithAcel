"use client";

import { useState, useEffect } from "react";
import Reveal from "@/components/ui/Reveal";
import { Markdown } from "@/lib/markdown";
import LearningModeModal from "./LearningModeModal";
import { Video, BookOpen } from "lucide-react";

interface LessonContentManagerProps {
  lesson: any;
}

export default function LessonContentManager({ lesson }: LessonContentManagerProps) {
  const [mode, setMode] = useState<string | null>(null); // "video", "text", or null (modal open)
  const [showModal, setShowModal] = useState(false);

  useEffect(() => {
    // Only show modal if lesson has a video and user hasn't set a preference
    const savedMode = localStorage.getItem("preferred_learn_mode");
    if (lesson.video_url) {
      if (savedMode === "video" || savedMode === "text") {
        setMode(savedMode);
      } else {
        setShowModal(true);
      }
    } else {
      setMode("text"); // Default to text if no video
    }
  }, [lesson.video_url]);

  const handleSelectMode = (selectedMode: string, remember: boolean) => {
    setMode(selectedMode);
    if (remember) {
      localStorage.setItem("preferred_learn_mode", selectedMode);
    }
  };

  const handleToggleMode = () => {
    const newMode = mode === "video" ? "text" : "video";
    setMode(newMode);
    // Optionally update local storage if they toggle manually? 
    // Usually manual toggle doesn't overwrite preference unless explicitly asked, but for simplicity, let's update it.
    localStorage.setItem("preferred_learn_mode", newMode);
  };

  if (mode === null) {
    // Initial loading or waiting for modal decision
    return (
      <>
        <LearningModeModal 
          isOpen={showModal} 
          onClose={() => {
            // Default to text if they just close it without selecting
            setShowModal(false);
            if (!mode) setMode("text");
          }} 
          onSelectMode={handleSelectMode} 
        />
        {/* Placeholder while waiting */}
        <div className="mt-8 animate-pulse rounded-2xl bg-white/5 h-96 w-full" />
      </>
    );
  }

  return (
    <div className="relative">
      {/* Mode Toggle Button */}
      {lesson.video_url && (
        <div className="mb-6 flex justify-end">
          <button
            onClick={handleToggleMode}
            className="group flex items-center gap-2 rounded-full border border-white/10 bg-white/5 px-4 py-2 text-sm font-medium text-muted-foreground transition-all hover:bg-white/10 hover:text-foreground"
          >
            {mode === "video" ? (
              <>
                <BookOpen size={16} className="text-emerald-400" />
                <span>Switch to Text Mode</span>
              </>
            ) : (
              <>
                <Video size={16} className="text-accent" />
                <span>Switch to Video Mode</span>
              </>
            )}
          </button>
        </div>
      )}

      {/* Video Mode Content */}
      {mode === "video" && lesson.video_url && (
        <Reveal delay={0.2} className="">
          <div className="mb-10 aspect-video w-full overflow-hidden rounded-2xl border border-white/10 bg-black/50 shadow-2xl">
            <iframe
              src={lesson.video_url}
              title={lesson.title}
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen
              className="h-full w-full border-none"
            />
          </div>
          {/* Optional: Add a brief note that text is available */}
          <p className="text-center text-sm text-muted-foreground">
            Ingin membaca materi lengkap? Klik &quot;Switch to Text Mode&quot; di bagian atas.
          </p>
        </Reveal>
      )}

      {/* Text Mode Content */}
      {mode === "text" && (
        <Reveal delay={0.2} className="">
          <div className="mt-2">
            <Markdown source={lesson.content} />
          </div>
        </Reveal>
      )}
    </div>
  );
}
