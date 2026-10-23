"use client";
import { useEffect, useRef, useState } from "react";

export function SoundControl() {
  const [playing, setPlaying] = useState(false);
  const [error, setError] = useState(false);
  const audio = useRef<AudioContext | null>(null);
  useEffect(() => {
    const stop = () => {
      if (document.hidden) {
        void audio.current?.close();
        audio.current = null;
        setPlaying(false);
      }
    };
    document.addEventListener("visibilitychange", stop);
    return () => {
      document.removeEventListener("visibilitychange", stop);
      void audio.current?.close();
    };
  }, []);
  async function toggle() {
    if (audio.current) {
      void audio.current.close();
      audio.current = null;
      setPlaying(false);
      return;
    }
    try {
      const context = new AudioContext();
      audio.current = context;
      await context.resume();
      if (audio.current !== context) return;
      const volume = context.createGain();
      volume.gain.setValueAtTime(0, context.currentTime);
      volume.gain.linearRampToValueAtTime(0.025, context.currentTime + 1.5);
      volume.connect(context.destination);
      [130.81, 196, 261.63, 329.63].forEach((frequency, index) => {
        const oscillator = context.createOscillator();
        oscillator.type = "sine";
        oscillator.frequency.value = frequency;
        oscillator.detune.value = index % 2 ? 4 : -4;
        oscillator.connect(volume);
        oscillator.start();
      });
      setPlaying(true);
      setError(false);
    } catch {
      setError(true);
      setPlaying(false);
      void audio.current?.close();
      audio.current = null;
    }
  }
  return (
    <div className="sound-control">
      <button onClick={toggle} className="sound-button" aria-pressed={playing}>
        <span
          className={`equalizer ${playing ? "playing" : ""}`}
          aria-hidden="true"
        >
          {[0, 1, 2, 3, 4].map((i) => (
            <i key={i} />
          ))}
        </span>
        {playing ? "Выключить атмосферу" : "Включить атмосферу"}
        <span className="sound-status">{playing ? "Вкл" : "Выкл"}</span>
      </button>
      <p aria-live="polite">
        {error
          ? "Не удалось включить звук в этом браузере."
          : "Синтезированный эмбиент. Не запись звучания наушников."}
      </p>
    </div>
  );
}
