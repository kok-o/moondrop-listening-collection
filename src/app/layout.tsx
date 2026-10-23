import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "MOONDROP — Между звуком и чувством",
  description:
    "Авторская витрина MOONDROP: COSMO, DUSK и SPACE TRAVEL. Точная инженерия, искусство слушать и Mitsuki Yuki. Некоммерческий fan concept.",
};
export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="ru">
      <body>{children}</body>
    </html>
  );
}
