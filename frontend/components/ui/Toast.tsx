"use client";

import { useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { CheckCircle2, XCircle } from "lucide-react";

interface ToastProps {
  show: boolean;
  isCorrect: boolean;
  message: string;
  onClose: () => void;
}

export function Toast({ show, isCorrect, message, onClose }: ToastProps) {
  useEffect(() => {
    if (!show) return;
    const timer = setTimeout(onClose, 3000);
    return () => clearTimeout(timer);
  }, [show, onClose]);

  return (
    <AnimatePresence>
      {show && (
        <motion.div
          initial={{ opacity: 0, y: 60 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: 60 }}
          className="fixed bottom-6 left-1/2 z-50 -translate-x-1/2"
        >
          <div
            className={`flex items-center gap-3 rounded-2xl px-6 py-4 shadow-lg backdrop-blur-md ${
              isCorrect
                ? "bg-emerald-500/95 text-white shadow-emerald-500/30"
                : "bg-red-500/95 text-white shadow-red-500/30"
            }`}
          >
            {isCorrect ? (
              <CheckCircle2 className="h-6 w-6 shrink-0" />
            ) : (
              <XCircle className="h-6 w-6 shrink-0" />
            )}
            <div>
              <p className="font-bold text-lg">
                {isCorrect ? "太棒了！" : "再想想哦"}
              </p>
              {message && (
                <p className="text-sm opacity-90 max-w-sm">{message}</p>
              )}
            </div>
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
