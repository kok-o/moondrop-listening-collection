"use client";
import { useEffect } from "react";

export function MotionDirector() {
  useEffect(() => {
    let disposed = false;
    let dispose: (() => void) | undefined;
    const preference = window.matchMedia("(prefers-reduced-motion: reduce)");
    let generation = 0;
    async function initialize() {
      const current = ++generation;
      dispose?.();
      dispose = undefined;
      if (preference.matches) return;
      const [{ gsap }, { ScrollTrigger }, { default: Lenis }] =
        await Promise.all([
          import("gsap"),
          import("gsap/ScrollTrigger"),
          import("lenis"),
        ]);
      if (disposed || current !== generation) return;
      gsap.registerPlugin(ScrollTrigger);
      const media = gsap.matchMedia();
      const lenis = new Lenis({
        duration: 1.05,
        smoothWheel: true,
        syncTouch: false,
        anchors: true,
        prevent: (node) => !!node.closest('[role="dialog"]'),
      });
      const update = () => ScrollTrigger.update();
      lenis.on("scroll", update);
      const tick = (time: number) => lenis.raf(time * 1000);
      gsap.ticker.add(tick);
      media.add("(min-width: 901px)", () => {
        const scene = document.querySelector(".hero-stage");
        if (!scene) return;
        const timeline = gsap.timeline({
          scrollTrigger: {
            trigger: scene,
            start: "top top",
            end: "bottom bottom",
            scrub: 0.7,
            invalidateOnRefresh: true,
          },
        });
        timeline
          .fromTo(
            ".hero-copy, .hero-bottom, .art-caption",
            { opacity: 1, y: 0 },
            { opacity: 0, y: -25, duration: 0.3 },
            0,
          )
          .fromTo(
            ".yuki-art",
            { x: 0, y: 0, opacity: 1 },
            { x: 110, y: -30, opacity: 0, duration: 0.65 },
            0,
          )
          .fromTo(
            ".hero-orbit",
            { scale: 1, opacity: 0.75 },
            { scale: 0.78, opacity: 0.3, duration: 0.8 },
            0,
          )
          .fromTo(
            ".hero-word",
            { y: 0, opacity: 1 },
            { y: -45, opacity: 0.09, duration: 0.7 },
            0,
          )
          .fromTo(
            ".hero-product",
            { x: 0, y: 0, scale: 1, rotation: -8 },
            {
              x: () => window.innerWidth * -0.235,
              y: () => -window.innerHeight * 0.06,
              scale: 1.38,
              rotation: 8,
              duration: 0.85,
              ease: "none",
            },
            0,
          )
          .fromTo(
            ".handoff-copy",
            { opacity: 0, y: 25 },
            { opacity: 1, y: 0, duration: 0.35 },
            0.55,
          );
      });
      media.add("(max-width: 900px)", () => {
        gsap.to(".yuki-art", {
          y: -25,
          ease: "none",
          scrollTrigger: {
            trigger: ".hero-stage",
            start: "top top",
            end: "bottom top",
            scrub: true,
          },
        });
      });
      gsap.to(".sound-wave", {
        xPercent: 3,
        ease: "none",
        scrollTrigger: {
          trigger: ".sound-scene",
          start: "top bottom",
          end: "bottom top",
          scrub: 1,
        },
      });
      const refresh = () => ScrollTrigger.refresh();
      document.fonts.ready.then(() => {
        if (!disposed && current === generation) refresh();
      });
      dispose = () => {
        media.revert();
        ScrollTrigger.getAll()
          .filter((t) => t.trigger?.classList.contains("sound-scene"))
          .forEach((t) => t.kill());
        gsap.ticker.remove(tick);
        lenis.off("scroll", update);
        lenis.destroy();
        gsap.set(".sound-wave", { clearProps: "transform" });
      };
    }
    void initialize();
    preference.addEventListener("change", initialize);
    return () => {
      disposed = true;
      generation++;
      preference.removeEventListener("change", initialize);
      dispose?.();
    };
  }, []);
  return null;
}
