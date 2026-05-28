"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";

export default function LearnRedirect() {
  const router = useRouter();
  useEffect(() => {
    router.replace("/learn/1");
  }, [router]);
  return null;
}
