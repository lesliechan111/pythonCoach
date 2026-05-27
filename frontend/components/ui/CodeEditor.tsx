"use client";

import Editor, { type OnMount } from "@monaco-editor/react";
import { cn } from "@/lib/utils";

interface CodeEditorProps {
  value: string;
  onChange?: (value: string) => void;
  readOnly?: boolean;
  height?: string;
  showBorder?: boolean;
  className?: string;
}

export function CodeEditor({
  value,
  onChange,
  readOnly = false,
  height = "250px",
  showBorder = true,
  className,
}: CodeEditorProps) {
  const handleMount: OnMount = (editor, monaco) => {
    monaco.editor.defineTheme("pythoncoach-dark", {
      base: "vs-dark",
      inherit: true,
      rules: [
        { token: "comment", foreground: "6A9955", fontStyle: "italic" },
        { token: "keyword", foreground: "569CD6" },
        { token: "string", foreground: "CE9178" },
        { token: "number", foreground: "B5CEA8" },
        { token: "type", foreground: "4EC9B0" },
        { token: "function", foreground: "DCDCAA" },
      ],
      colors: {
        "editor.background": "#09090b",
        "editor.foreground": "#e4e4e7",
        "editor.lineHighlightBackground": "#18181b",
        "editor.selectionBackground": "#264f78",
        "editor.inactiveSelectionBackground": "#3a3d41",
        "editorCursor.foreground": "#e4e4e7",
        "editorLineNumber.foreground": "#52525b",
        "editorLineNumber.activeForeground": "#a1a1aa",
      },
    });

    monaco.editor.setTheme("pythoncoach-dark");

    editor.updateOptions({
      fontSize: 14,
      fontFamily: "'JetBrains Mono', 'Fira Code', 'Cascadia Code', monospace",
      minimap: { enabled: false },
      scrollBeyondLastLine: false,
      lineNumbers: "on",
      renderLineHighlight: "line",
      folding: true,
      tabSize: 4,
      insertSpaces: true,
      automaticLayout: true,
      wordWrap: "on",
      padding: { top: 12, bottom: 12 },
      readOnly,
    });

    setTimeout(() => editor.focus(), 100);
  };

  return (
    <div
      className={cn(
        showBorder && "overflow-hidden rounded-xl border border-zinc-800",
        className
      )}
    >
      <Editor
        height={height}
        language="python"
        value={value}
        onChange={(v) => onChange?.(v || "")}
        onMount={handleMount}
        loading={
          <div className="flex h-full items-center justify-center bg-zinc-950 text-sm text-zinc-500">
            Loading...
          </div>
        }
        options={{
          readOnly,
          automaticLayout: true,
        }}
      />
    </div>
  );
}
