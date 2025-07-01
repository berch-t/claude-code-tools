# Aceternity UI - Modern React Components

Aceternity UI is a collection of modern, animated React components built with Tailwind CSS and Framer Motion. It provides beautiful, customizable components for building stunning user interfaces.

## Installation

```bash
# Install Aceternity UI
npm install @aceternity/ui

# Required peer dependencies
npm install framer-motion clsx tailwind-merge
```

## Setup

### 1. Tailwind CSS Configuration

```js
// tailwind.config.js
module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./node_modules/@aceternity/ui/**/*.{js,ts,jsx,tsx}"
  ],
  theme: {
    extend: {
      animation: {
        "meteor-effect": "meteor 5s linear infinite",
        "gradient": "gradient 8s linear infinite",
        "shimmer": "shimmer 2s linear infinite"
      },
      keyframes: {
        meteor: {
          "0%": { transform: "rotate(215deg) translateX(0)", opacity: "1" },
          "70%": { opacity: "1" },
          "100%": { transform: "rotate(215deg) translateX(-500px)", opacity: "0" }
        }
      }
    }
  },
  plugins: []
}
```

### 2. CSS Variables

```css
/* globals.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --background: 0 0% 100%;
  --foreground: 222.2 84% 4.9%;
  --primary: 222.2 47.4% 11.2%;
  --primary-foreground: 210 40% 98%;
}

.dark {
  --background: 222.2 84% 4.9%;
  --foreground: 210 40% 98%;
  --primary: 210 40% 98%;
  --primary-foreground: 222.2 47.4% 11.2%;
}
```

## Core Components

### 1. Hero Section

```tsx
import { HeroHighlight, Highlight } from "@aceternity/ui/hero-highlight";

export function HeroSection() {
  return (
    <HeroHighlight>
      <h1 className="text-4xl lg:text-6xl font-bold text-neutral-700 dark:text-white max-w-4xl leading-relaxed lg:leading-snug text-center mx-auto">
        Build amazing{" "}
        <Highlight className="text-black dark:text-white">
          user interfaces
        </Highlight>{" "}
        with Aceternity UI
      </h1>
    </HeroHighlight>
  );
}
```

### 2. Spotlight Effect

```tsx
import { Spotlight } from "@aceternity/ui/spotlight";

export function SpotlightPreview() {
  return (
    <div className="h-[40rem] w-full rounded-md flex md:items-center md:justify-center bg-black/[0.96] antialiased bg-grid-white/[0.02] relative overflow-hidden">
      <Spotlight
        className="-top-40 left-0 md:left-60 md:-top-20"
        fill="white"
      />
      <div className="p-4 max-w-7xl mx-auto relative z-10 w-full pt-20 md:pt-0">
        <h1 className="text-4xl md:text-7xl font-bold text-center bg-clip-text text-transparent bg-gradient-to-b from-neutral-50 to-neutral-400 bg-opacity-50">
          Spotlight <br /> is the new trend.
        </h1>
      </div>
    </div>
  );
}
```

### 3. Animated Cards

```tsx
import { HoverEffect } from "@aceternity/ui/card-hover-effect";

export function CardHoverEffectDemo() {
  return (
    <div className="max-w-5xl mx-auto px-8">
      <HoverEffect items={projects} />
    </div>
  );
}

const projects = [
  {
    title: "Stripe",
    description: "A technology company that builds economic infrastructure for the internet.",
    link: "https://stripe.com"
  },
  {
    title: "Netflix",
    description: "A streaming service that offers a wide variety of award-winning TV shows, movies and documentaries.",
    link: "https://netflix.com"
  }
];
```

### 4. Floating Navbar

```tsx
import { FloatingNav } from "@aceternity/ui/floating-navbar";
import { IconHome, IconMessage, IconUser } from "@tabler/icons-react";

export function FloatingNavDemo() {
  const navItems = [
    {
      name: "Home",
      link: "/",
      icon: <IconHome className="h-4 w-4 text-neutral-500 dark:text-white" />
    },
    {
      name: "About",
      link: "/about",
      icon: <IconUser className="h-4 w-4 text-neutral-500 dark:text-white" />
    },
    {
      name: "Contact",
      link: "/contact",
      icon: <IconMessage className="h-4 w-4 text-neutral-500 dark:text-white" />
    }
  ];
  
  return (
    <div className="relative w-full">
      <FloatingNav navItems={navItems} />
    </div>
  );
}
```

### 5. Background Beams

```tsx
import { BackgroundBeams } from "@aceternity/ui/background-beams";

export function BackgroundBeamsDemo() {
  return (
    <div className="h-[40rem] w-full bg-neutral-950 relative flex flex-col items-center justify-center antialiased">
      <div className="max-w-2xl mx-auto p-4">
        <h1 className="relative z-10 text-lg md:text-7xl bg-clip-text text-transparent bg-gradient-to-b from-neutral-200 to-neutral-600 text-center font-sans font-bold">
          Join the waitlist
        </h1>
        <p className="text-neutral-500 max-w-lg mx-auto my-2 text-sm text-center relative z-10">
          Welcome to MailJet, the best transactional email service on the web.
        </p>
      </div>
      <BackgroundBeams />
    </div>
  );
}
```

### 6. Infinite Moving Cards

```tsx
import { InfiniteMovingCards } from "@aceternity/ui/infinite-moving-cards";

export function InfiniteMovingCardsDemo() {
  return (
    <div className="h-[40rem] rounded-md flex flex-col antialiased bg-white dark:bg-black dark:bg-grid-white/[0.05] items-center justify-center relative overflow-hidden">
      <InfiniteMovingCards
        items={testimonials}
        direction="right"
        speed="slow"
      />
    </div>
  );
}

const testimonials = [
  {
    quote: "It was the best of times, it was the worst of times...",
    name: "Charles Dickens",
    title: "A Tale of Two Cities"
  }
];
```

### 7. Meteors Effect

```tsx
import { Meteors } from "@aceternity/ui/meteors";

export function MeteorsDemo() {
  return (
    <div className="w-full relative max-w-xs">
      <div className="absolute inset-0 h-full w-full bg-gradient-to-r from-blue-500 to-teal-500 transform scale-[0.80] bg-red-500 rounded-full blur-3xl" />
      <div className="relative shadow-xl bg-gray-900 border border-gray-800 px-4 py-8 h-full overflow-hidden rounded-2xl flex flex-col justify-end items-start">
        <div className="h-5 w-5 rounded-full border flex items-center justify-center mb-4 border-gray-500">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            strokeWidth="1.5"
            stroke="currentColor"
            className="h-2 w-2 text-gray-300"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              d="M4.5 4.5l15 15m0 0V8.25m0 11.25H8.25"
            />
          </svg>
        </div>

        <h1 className="font-bold text-xl text-white mb-4 relative z-50">
          Meteors because they&apos;re cool
        </h1>

        <p className="font-normal text-base text-slate-500 mb-4 relative z-50">
          I don&apos;t know what to write so I&apos;ll just paste something
          cool here. One more sentence because lorem ipsum is overrated.
        </p>

        <button className="border px-4 py-1 rounded-lg border-gray-500 text-gray-300">
          Explore
        </button>

        <Meteors number={20} />
      </div>
    </div>
  );
}
```

## TypeScript Integration

### Component Props Interface

```tsx
import { ReactNode } from "react";

interface AceternityComponentProps {
  children?: ReactNode;
  className?: string;
  animate?: boolean;
  duration?: number;
  delay?: number;
}

// Example usage with custom component
interface CustomHeroProps extends AceternityComponentProps {
  title: string;
  subtitle?: string;
  backgroundImage?: string;
}

const CustomHero: React.FC<CustomHeroProps> = ({
  title,
  subtitle,
  className,
  animate = true,
  ...props
}) => {
  return (
    <HeroHighlight className={className} {...props}>
      <h1>{title}</h1>
      {subtitle && <p>{subtitle}</p>}
    </HeroHighlight>
  );
};
```

## Best Practices

### 1. Performance Optimization

```tsx
import { memo, useCallback } from "react";
import { motion } from "framer-motion";

// Memoize heavy components
const OptimizedCard = memo(({ data }: { data: any }) => {
  const handleClick = useCallback(() => {
    // Handle click logic
  }, []);

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      onClick={handleClick}
    >
      {/* Card content */}
    </motion.div>
  );
});
```

### 2. Responsive Design

```tsx
import { useMediaQuery } from "@/hooks/use-media-query";

export function ResponsiveComponent() {
  const isMobile = useMediaQuery("(max-width: 768px)");
  
  return (
    <HoverEffect
      items={projects}
      className={isMobile ? "grid-cols-1" : "grid-cols-3"}
    />
  );
}
```

### 3. Theme Integration

```tsx
import { useTheme } from "next-themes";

export function ThemedComponent() {
  const { theme } = useTheme();
  
  return (
    <Spotlight
      fill={theme === "dark" ? "white" : "black"}
      className="spotlight-custom"
    />
  );
}
```

## Next.js Integration

### 1. Dynamic Imports

```tsx
import dynamic from "next/dynamic";

const BackgroundBeams = dynamic(
  () => import("@aceternity/ui/background-beams").then(mod => mod.BackgroundBeams),
  { ssr: false }
);

export default function Page() {
  return (
    <div>
      <BackgroundBeams />
    </div>
  );
}
```

### 2. App Router Setup

```tsx
// app/layout.tsx
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Aceternity UI App",
  description: "Built with Aceternity UI components"
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  );
}
```

## Common Patterns

### 1. Animation Variants

```tsx
const cardVariants = {
  hidden: { opacity: 0, y: 20 },
  visible: { 
    opacity: 1, 
    y: 0,
    transition: {
      duration: 0.6,
      ease: "easeOut"
    }
  }
};

export function AnimatedCard({ children }: { children: React.ReactNode }) {
  return (
    <motion.div
      variants={cardVariants}
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true }}
    >
      {children}
    </motion.div>
  );
}
```

### 2. Custom Hooks

```tsx
import { useEffect, useState } from "react";

export function useIntersectionObserver(ref: React.RefObject<Element>) {
  const [isIntersecting, setIsIntersecting] = useState(false);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => setIsIntersecting(entry.isIntersecting)
    );
    
    if (ref.current) {
      observer.observe(ref.current);
    }
    
    return () => observer.disconnect();
  }, [ref]);

  return isIntersecting;
}
```

## Troubleshooting

### Common Issues

1. **Hydration Errors**: Use dynamic imports for client-only components
2. **Animation Performance**: Use `transform` and `opacity` properties
3. **Bundle Size**: Import components individually to enable tree shaking

### Error Handling

```tsx
import { ErrorBoundary } from "react-error-boundary";

function ErrorFallback({ error }: { error: Error }) {
  return (
    <div className="text-red-500 p-4">
      <h2>Something went wrong:</h2>
      <pre>{error.message}</pre>
    </div>
  );
}

export function SafeAceternityComponent() {
  return (
    <ErrorBoundary FallbackComponent={ErrorFallback}>
      <HeroHighlight>
        {/* Component content */}
      </HeroHighlight>
    </ErrorBoundary>
  );
}
```

## Resources

- [Official Documentation](https://ui.aceternity.com)
- [GitHub Repository](https://github.com/aceternity/ui)
- [Component Examples](https://ui.aceternity.com/components)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Framer Motion Documentation](https://www.framer.com/motion/)