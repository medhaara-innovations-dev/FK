import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";
import "./hero.css";
import "./why.css";
import "./how.css";
import "./uses.css";
import "./security.css";
import "./cta.css";
import "./motion.css";
import { MOTION_BOOT } from "@/lib/motion";

const poppins = localFont({
  src: [
    { path: "./fonts/Poppins-Medium.ttf", weight: "500", style: "normal" },
    { path: "./fonts/Poppins-SemiBold.ttf", weight: "600", style: "normal" },
    { path: "./fonts/Poppins-Bold.ttf", weight: "700", style: "normal" },
  ],
  variable: "--font-poppins",
  display: "swap",
});

const mulish = localFont({
  src: [
    { path: "./fonts/Mulish-Regular.ttf", weight: "400", style: "normal" },
    { path: "./fonts/Mulish-SemiBold.ttf", weight: "600", style: "normal" },
  ],
  variable: "--font-mulish",
  display: "swap",
});

export const metadata: Metadata = {
  title: "FamilyKit · Everything in place.",
  description:
    "Everything important, in one place. You don't have to remember where everything is. FamilyKit remembers for you.",
  icons: {
    icon: [
      { url: "/favicon.ico" },
      { url: "/favicon.svg", type: "image/svg+xml" },
      { url: "/favicon-32.png", sizes: "32x32", type: "image/png" },
    ],
    apple: "/apple-touch-icon.png",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html
      lang="en"
      suppressHydrationWarning
      className={`${poppins.variable} ${mulish.variable} h-full antialiased`}
    >
      <head>
        <script dangerouslySetInnerHTML={{ __html: MOTION_BOOT }} />
      </head>
      <body className="min-h-full">{children}</body>
    </html>
  );
}
