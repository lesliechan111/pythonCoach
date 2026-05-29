"use client";

import { useState, useEffect, useRef } from "react";

export function useCountUp(target: number, duration = 800): number {
  const [value, setValue] = useState(0);
  const prevTarget = useRef(0);
  const frameRef = useRef<number>(0);

  useEffect(() => {
    const startValue = prevTarget.current;
    const diff = target - startValue;
    if (diff === 0) {
      setValue(target);
      return;
    }
    const startTime = performance.now();

    function tick(now: number) {
      const elapsed = now - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3); // easeOutCubic
      setValue(startValue + diff * eased);
      if (progress < 1) {
        frameRef.current = requestAnimationFrame(tick);
      }
    }

    frameRef.current = requestAnimationFrame(tick);
    prevTarget.current = target;

    return () => cancelAnimationFrame(frameRef.current);
  }, [target, duration]);

  return value;
}
