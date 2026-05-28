"use client";

import { Component } from "react";
import { AlertTriangle, RefreshCw } from "lucide-react";

interface Props {
  children: React.ReactNode;
}

interface State {
  hasError: boolean;
  error?: Error;
}

export class ErrorBoundary extends Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error: Error): State {
    return { hasError: true, error };
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="flex h-[calc(100vh-4rem)] items-center justify-center p-4">
          <div className="text-center max-w-md">
            <div className="flex justify-center mb-4">
              <AlertTriangle className="h-12 w-12 text-yellow-500" />
            </div>
            <h2 className="text-xl font-bold">页面出错了</h2>
            <p className="mt-2 text-sm text-muted-foreground">
              页面渲染时发生了意外错误，请尝试刷新重试。
            </p>
            {process.env.NODE_ENV === "development" && this.state.error && (
              <pre className="mt-4 rounded-lg bg-muted p-3 text-xs text-left overflow-x-auto whitespace-pre-wrap">
                {this.state.error.message}
              </pre>
            )}
            <button
              onClick={() => this.setState({ hasError: false })}
              className="mt-6 inline-flex items-center gap-2 rounded-lg bg-primary px-5 py-2.5 text-sm font-medium text-primary-foreground hover:opacity-90"
            >
              <RefreshCw className="h-4 w-4" />
              重试
            </button>
          </div>
        </div>
      );
    }

    return this.props.children;
  }
}
