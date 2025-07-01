# Framer Motion - Advanced React Animations

Framer Motion is a powerful animation library for React that makes it easy to create fluid, performant animations and gestures. This guide covers the latest features, patterns, and best practices for Framer Motion.

## Installation & Setup

```bash
# Install Framer Motion
npm install framer-motion

# TypeScript support is included
npm install @types/react @types/react-dom
```

## Basic Setup

### 1. Simple Animation

```tsx
import { motion } from 'framer-motion';

export function BasicAnimation() {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="p-6 bg-blue-500 text-white rounded-lg"
    >
      Hello Framer Motion!
    </motion.div>
  );
}
```

### 2. Hover and Tap Animations

```tsx
import { motion } from 'framer-motion';

export function InteractiveButton() {
  return (
    <motion.button
      whileHover={{ scale: 1.05 }}
      whileTap={{ scale: 0.95 }}
      className="px-6 py-3 bg-purple-500 text-white rounded-lg font-medium"
    >
      Click me!
    </motion.button>
  );
}
```

## Animation Variants

### 1. Variant System

```tsx
import { motion, Variants } from 'framer-motion';

const containerVariants: Variants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      delayChildren: 0.3,
      staggerChildren: 0.2
    }
  }
};

const itemVariants: Variants = {
  hidden: { y: 20, opacity: 0 },
  visible: {
    y: 0,
    opacity: 1,
    transition: {
      type: "spring",
      stiffness: 100
    }
  }
};

export function StaggeredList() {
  const items = ['Item 1', 'Item 2', 'Item 3', 'Item 4'];

  return (
    <motion.ul
      variants={containerVariants}
      initial="hidden"
      animate="visible"
      className="space-y-2"
    >
      {items.map((item, index) => (
        <motion.li
          key={index}
          variants={itemVariants}
          className="p-4 bg-gray-100 rounded-lg"
        >
          {item}
        </motion.li>
      ))}
    </motion.ul>
  );
}
```

### 2. Complex Variants with TypeScript

```tsx
import { motion, Variants } from 'framer-motion';

interface CardProps {
  title: string;
  description: string;
  isSelected: boolean;
  onClick: () => void;
}

const cardVariants: Variants = {
  unselected: {
    scale: 1,
    backgroundColor: "#ffffff",
    transition: { duration: 0.2 }
  },
  selected: {
    scale: 1.02,
    backgroundColor: "#f3f4f6",
    transition: { duration: 0.2 }
  },
  hover: {
    scale: 1.05,
    transition: { duration: 0.1 }
  }
};

export function AnimatedCard({ title, description, isSelected, onClick }: CardProps) {
  return (
    <motion.div
      variants={cardVariants}
      initial="unselected"
      animate={isSelected ? "selected" : "unselected"}
      whileHover="hover"
      onClick={onClick}
      className="p-6 border rounded-lg cursor-pointer"
    >
      <h3 className="text-lg font-semibold">{title}</h3>
      <p className="text-gray-600">{description}</p>
    </motion.div>
  );
}
```

## Layout Animations

### 1. Automatic Layout Animations

```tsx
import { motion, AnimatePresence } from 'framer-motion';
import { useState } from 'react';

export function LayoutAnimation() {
  const [isExpanded, setIsExpanded] = useState(false);

  return (
    <motion.div
      layout
      className="p-6 bg-white border rounded-lg cursor-pointer"
      onClick={() => setIsExpanded(!isExpanded)}
    >
      <motion.h2 layout className="text-xl font-bold mb-4">
        Click to expand
      </motion.h2>
      
      <AnimatePresence>
        {isExpanded && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: 'auto' }}
            exit={{ opacity: 0, height: 0 }}
            transition={{ duration: 0.3 }}
          >
            <p className="text-gray-600">
              This content animates in and out smoothly with layout animations.
              The parent container automatically adjusts its size.
            </p>
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  );
}
```

### 2. Shared Layout Animations

```tsx
import { motion } from 'framer-motion';
import { useState } from 'react';

interface Item {
  id: string;
  title: string;
  category: string;
}

export function SharedLayoutAnimation() {
  const [selectedCategory, setSelectedCategory] = useState('all');
  
  const items: Item[] = [
    { id: '1', title: 'React', category: 'frontend' },
    { id: '2', title: 'Node.js', category: 'backend' },
    { id: '3', title: 'TypeScript', category: 'frontend' },
    { id: '4', title: 'PostgreSQL', category: 'database' },
  ];

  const categories = ['all', 'frontend', 'backend', 'database'];
  
  const filteredItems = selectedCategory === 'all' 
    ? items 
    : items.filter(item => item.category === selectedCategory);

  return (
    <div>
      <div className="flex gap-2 mb-6">
        {categories.map(category => (
          <button
            key={category}
            onClick={() => setSelectedCategory(category)}
            className={`px-4 py-2 rounded-lg relative ${
              selectedCategory === category 
                ? 'text-white' 
                : 'text-gray-600 hover:text-gray-900'
            }`}
          >
            {selectedCategory === category && (
              <motion.div
                layoutId="activeCategory"
                className="absolute inset-0 bg-blue-500 rounded-lg"
                transition={{ type: "spring", stiffness: 300, damping: 30 }}
              />
            )}
            <span className="relative z-10 capitalize">{category}</span>
          </button>
        ))}
      </div>

      <motion.div layout className="grid grid-cols-2 gap-4">
        {filteredItems.map(item => (
          <motion.div
            key={item.id}
            layout
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            exit={{ opacity: 0, scale: 0.8 }}
            className="p-4 bg-gray-100 rounded-lg"
          >
            <h3 className="font-semibold">{item.title}</h3>
            <p className="text-sm text-gray-600">{item.category}</p>
          </motion.div>
        ))}
      </motion.div>
    </div>
  );
}
```

## Gestures & Interactions

### 1. Drag Gestures

```tsx
import { motion, PanInfo } from 'framer-motion';
import { useState } from 'react';

export function DragExample() {
  const [position, setPosition] = useState({ x: 0, y: 0 });

  const handleDragEnd = (event: MouseEvent | TouchEvent | PointerEvent, info: PanInfo) => {
    // Snap to grid
    const snapToGrid = (value: number, gridSize: number = 50) => {
      return Math.round(value / gridSize) * gridSize;
    };

    setPosition({
      x: snapToGrid(info.offset.x),
      y: snapToGrid(info.offset.y)
    });
  };

  return (
    <div className="h-96 bg-gray-100 rounded-lg relative overflow-hidden">
      <motion.div
        drag
        dragConstraints={{ left: 0, top: 0, right: 300, bottom: 300 }}
        dragElastic={0.2}
        onDragEnd={handleDragEnd}
        animate={position}
        className="w-16 h-16 bg-blue-500 rounded-lg cursor-grab active:cursor-grabbing flex items-center justify-center text-white font-bold"
        whileDrag={{ scale: 1.1 }}
      >
        Drag
      </motion.div>
    </div>
  );
}
```

### 2. Advanced Gestures

```tsx
import { motion, useMotionValue, useTransform } from 'framer-motion';

export function AdvancedGestures() {
  const x = useMotionValue(0);
  const background = useTransform(
    x,
    [-100, 0, 100],
    ["#ff008c", "#7700ff", "#ff0000"]
  );

  return (
    <motion.div
      className="h-32 rounded-lg cursor-grab active:cursor-grabbing flex items-center justify-center text-white font-bold"
      style={{ background }}
      drag="x"
      dragConstraints={{ left: -100, right: 100 }}
      style={{ x }}
      whileTap={{ scale: 0.95 }}
    >
      Drag horizontally
    </motion.div>
  );
}
```

## Page Transitions

### 1. Route Transitions

```tsx
import { motion, AnimatePresence } from 'framer-motion';
import { useRouter } from 'next/router';

const pageVariants = {
  initial: {
    opacity: 0,
    x: "-100vw",
    scale: 0.8
  },
  in: {
    opacity: 1,
    x: 0,
    scale: 1
  },
  out: {
    opacity: 0,
    x: "100vw",
    scale: 1.2
  }
};

const pageTransition = {
  type: "tween",
  ease: "anticipate",
  duration: 0.5
};

interface PageTransitionProps {
  children: React.ReactNode;
}

export function PageTransition({ children }: PageTransitionProps) {
  const router = useRouter();

  return (
    <AnimatePresence mode="wait">
      <motion.div
        key={router.pathname}
        initial="initial"
        animate="in"
        exit="out"
        variants={pageVariants}
        transition={pageTransition}
      >
        {children}
      </motion.div>
    </AnimatePresence>
  );
}
```

### 2. Modal Animations

```tsx
import { motion, AnimatePresence } from 'framer-motion';
import { useEffect } from 'react';

interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  children: React.ReactNode;
}

const backdropVariants = {
  visible: { opacity: 1 },
  hidden: { opacity: 0 }
};

const modalVariants = {
  hidden: {
    y: "-100vh",
    opacity: 0,
    scale: 0.5
  },
  visible: {
    y: "0",
    opacity: 1,
    scale: 1,
    transition: {
      duration: 0.3,
      type: "spring",
      damping: 25,
      stiffness: 500
    }
  },
  exit: {
    y: "100vh",
    opacity: 0,
    scale: 0.5,
    transition: {
      duration: 0.2
    }
  }
};

export function AnimatedModal({ isOpen, onClose, children }: ModalProps) {
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = 'unset';
    }
    
    return () => {
      document.body.style.overflow = 'unset';
    };
  }, [isOpen]);

  return (
    <AnimatePresence>
      {isOpen && (
        <motion.div
          className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50"
          variants={backdropVariants}
          initial="hidden"
          animate="visible"
          exit="hidden"
          onClick={onClose}
        >
          <motion.div
            className="bg-white rounded-lg p-6 max-w-md w-full mx-4"
            variants={modalVariants}
            initial="hidden"
            animate="visible"
            exit="exit"
            onClick={(e) => e.stopPropagation()}
          >
            {children}
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
```

## Advanced Patterns

### 1. Custom Hooks for Animations

```tsx
import { useAnimation, useInView } from 'framer-motion';
import { useEffect, useRef } from 'react';

// Scroll-triggered animations
export function useScrollAnimation() {
  const controls = useAnimation();
  const ref = useRef(null);
  const inView = useInView(ref, { once: true, margin: "-100px" });

  useEffect(() => {
    if (inView) {
      controls.start("visible");
    }
  }, [controls, inView]);

  return { ref, controls };
}

// Usage
export function ScrollAnimatedComponent() {
  const { ref, controls } = useScrollAnimation();

  return (
    <motion.div
      ref={ref}
      animate={controls}
      initial="hidden"
      variants={{
        hidden: { opacity: 0, y: 50 },
        visible: { opacity: 1, y: 0, transition: { duration: 0.6 } }
      }}
      className="p-6 bg-blue-500 text-white rounded-lg"
    >
      This animates when scrolled into view
    </motion.div>
  );
}

// Typewriter effect
export function useTypewriter(text: string, speed: number = 50) {
  const [displayedText, setDisplayedText] = useState('');
  const [isComplete, setIsComplete] = useState(false);

  useEffect(() => {
    if (displayedText.length < text.length) {
      const timeout = setTimeout(() => {
        setDisplayedText(text.slice(0, displayedText.length + 1));
      }, speed);
      return () => clearTimeout(timeout);
    } else {
      setIsComplete(true);
    }
  }, [displayedText, text, speed]);

  return { displayedText, isComplete };
}

export function TypewriterText({ text }: { text: string }) {
  const { displayedText, isComplete } = useTypewriter(text);

  return (
    <div className="font-mono text-xl">
      {displayedText}
      <motion.span
        animate={{ opacity: isComplete ? 0 : 1 }}
        transition={{ duration: 0.5, repeat: Infinity, repeatType: "reverse" }}
        className="inline-block"
      >
        |
      </motion.span>
    </div>
  );
}
```

### 2. Motion Values and Transforms

```tsx
import { motion, useMotionValue, useTransform, useSpring } from 'framer-motion';
import { useEffect } from 'react';

export function MotionValueExample() {
  const x = useMotionValue(0);
  const y = useMotionValue(0);
  
  // Transform values
  const rotateX = useTransform(y, [-200, 200], [30, -30]);
  const rotateY = useTransform(x, [-200, 200], [-30, 30]);
  
  // Spring animation
  const springX = useSpring(x, { stiffness: 100, damping: 30 });
  const springY = useSpring(y, { stiffness: 100, damping: 30 });

  useEffect(() => {
    const handleMouseMove = (event: MouseEvent) => {
      const rect = event.currentTarget.getBoundingClientRect();
      const centerX = rect.left + rect.width / 2;
      const centerY = rect.top + rect.height / 2;
      
      x.set(event.clientX - centerX);
      y.set(event.clientY - centerY);
    };

    const element = document.getElementById('motion-card');
    if (element) {
      element.addEventListener('mousemove', handleMouseMove);
      element.addEventListener('mouseleave', () => {
        x.set(0);
        y.set(0);
      });
      
      return () => {
        element.removeEventListener('mousemove', handleMouseMove);
      };
    }
  }, [x, y]);

  return (
    <div id="motion-card" className="flex items-center justify-center h-96">
      <motion.div
        className="w-32 h-32 bg-gradient-to-br from-purple-500 to-pink-500 rounded-xl"
        style={{
          rotateX,
          rotateY,
          transformStyle: "preserve-3d"
        }}
      />
    </div>
  );
}
```

### 3. Timeline Animations

```tsx
import { motion, useAnimation } from 'framer-motion';
import { useEffect } from 'react';

export function TimelineAnimation() {
  const controls = useAnimation();

  useEffect(() => {
    const sequence = async () => {
      await controls.start({
        scale: 1.2,
        transition: { duration: 0.5 }
      });
      
      await controls.start({
        rotateZ: 360,
        transition: { duration: 1 }
      });
      
      await controls.start({
        scale: 1,
        backgroundColor: "#10b981",
        transition: { duration: 0.5 }
      });
    };

    sequence();
  }, [controls]);

  return (
    <motion.div
      animate={controls}
      className="w-20 h-20 bg-blue-500 rounded-lg"
    />
  );
}
```

## Performance Optimization

### 1. Optimizing Animations

```tsx
import { motion, useMotionValue, useTransform } from 'framer-motion';
import { useCallback, useMemo } from 'react';

// Use transform instead of animating layout properties
export function OptimizedAnimation() {
  const x = useMotionValue(0);
  const y = useMotionValue(0);
  
  // Memoize transforms to prevent unnecessary recalculations
  const rotate = useTransform(x, [-100, 100], [-45, 45]);
  const scale = useTransform(y, [-100, 100], [0.8, 1.2]);

  return (
    <motion.div
      drag
      style={{ x, y, rotate, scale }}
      className="w-20 h-20 bg-red-500 rounded-lg"
      // Use will-change for better performance
      whileDrag={{ willChange: "transform" }}
    />
  );
}

// Reduce motion for accessibility
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

export function AccessibleAnimation() {
  const shouldReduceMotion = reduceMotion.matches;

  return (
    <motion.div
      initial={shouldReduceMotion ? {} : { opacity: 0, y: 20 }}
      animate={shouldReduceMotion ? {} : { opacity: 1, y: 0 }}
      transition={shouldReduceMotion ? { duration: 0 } : { duration: 0.5 }}
      className="p-4 bg-green-500 text-white rounded-lg"
    >
      Respects user motion preferences
    </motion.div>
  );
}
```

### 2. Memory Management

```tsx
import { motion, AnimatePresence } from 'framer-motion';
import { useState, useCallback } from 'react';

interface ListItem {
  id: string;
  content: string;
}

export function OptimizedList() {
  const [items, setItems] = useState<ListItem[]>([]);

  const addItem = useCallback(() => {
    const newItem: ListItem = {
      id: Date.now().toString(),
      content: `Item ${items.length + 1}`
    };
    setItems(prev => [...prev, newItem]);
  }, [items.length]);

  const removeItem = useCallback((id: string) => {
    setItems(prev => prev.filter(item => item.id !== id));
  }, []);

  return (
    <div>
      <button onClick={addItem} className="mb-4 px-4 py-2 bg-blue-500 text-white rounded">
        Add Item
      </button>
      
      <AnimatePresence>
        {items.map(item => (
          <motion.div
            key={item.id}
            layout
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: 'auto' }}
            exit={{ opacity: 0, height: 0 }}
            transition={{ duration: 0.2 }}
            className="p-4 mb-2 bg-gray-100 rounded flex justify-between items-center"
          >
            <span>{item.content}</span>
            <button
              onClick={() => removeItem(item.id)}
              className="px-2 py-1 bg-red-500 text-white rounded text-sm"
            >
              Remove
            </button>
          </motion.div>
        ))}
      </AnimatePresence>
    </div>
  );
}
```

## Common Animation Patterns

### 1. Loading Animations

```tsx
import { motion } from 'framer-motion';

export function LoadingSpinner() {
  return (
    <motion.div
      className="w-8 h-8 border-2 border-gray-300 border-t-blue-500 rounded-full"
      animate={{ rotate: 360 }}
      transition={{ duration: 1, repeat: Infinity, ease: "linear" }}
    />
  );
}

export function LoadingDots() {
  const dotVariants = {
    initial: { y: 0 },
    animate: { y: -10 }
  };

  return (
    <div className="flex space-x-1">
      {[0, 1, 2].map(i => (
        <motion.div
          key={i}
          className="w-2 h-2 bg-blue-500 rounded-full"
          variants={dotVariants}
          initial="initial"
          animate="animate"
          transition={{
            duration: 0.6,
            repeat: Infinity,
            repeatType: "reverse",
            delay: i * 0.2
          }}
        />
      ))}
    </div>
  );
}

export function LoadingProgress({ progress }: { progress: number }) {
  return (
    <div className="w-full bg-gray-200 rounded-full h-2">
      <motion.div
        className="bg-blue-500 h-2 rounded-full"
        initial={{ width: 0 }}
        animate={{ width: `${progress}%` }}
        transition={{ duration: 0.5, ease: "easeOut" }}
      />
    </div>
  );
}
```

### 2. Notification Animations

```tsx
import { motion, AnimatePresence } from 'framer-motion';
import { useState, useEffect } from 'react';

interface Notification {
  id: string;
  message: string;
  type: 'success' | 'error' | 'info';
}

export function NotificationSystem() {
  const [notifications, setNotifications] = useState<Notification[]>([]);

  const addNotification = (message: string, type: Notification['type']) => {
    const notification: Notification = {
      id: Date.now().toString(),
      message,
      type
    };
    setNotifications(prev => [...prev, notification]);

    // Auto remove after 5 seconds
    setTimeout(() => {
      setNotifications(prev => prev.filter(n => n.id !== notification.id));
    }, 5000);
  };

  const removeNotification = (id: string) => {
    setNotifications(prev => prev.filter(n => n.id !== id));
  };

  return (
    <div className="fixed top-4 right-4 z-50 space-y-2">
      <AnimatePresence>
        {notifications.map(notification => (
          <motion.div
            key={notification.id}
            initial={{ opacity: 0, x: 300, scale: 0.3 }}
            animate={{ opacity: 1, x: 0, scale: 1 }}
            exit={{ opacity: 0, x: 300, scale: 0.5 }}
            transition={{ duration: 0.3 }}
            className={`p-4 rounded-lg shadow-lg max-w-sm ${
              notification.type === 'success' ? 'bg-green-500' :
              notification.type === 'error' ? 'bg-red-500' :
              'bg-blue-500'
            } text-white`}
          >
            <div className="flex justify-between items-center">
              <p>{notification.message}</p>
              <button
                onClick={() => removeNotification(notification.id)}
                className="ml-2 text-white hover:text-gray-200"
              >
                ×
              </button>
            </div>
          </motion.div>
        ))}
      </AnimatePresence>
      
      <div className="space-x-2">
        <button
          onClick={() => addNotification('Success message!', 'success')}
          className="px-4 py-2 bg-green-500 text-white rounded"
        >
          Success
        </button>
        <button
          onClick={() => addNotification('Error message!', 'error')}
          className="px-4 py-2 bg-red-500 text-white rounded"
        >
          Error
        </button>
      </div>
    </div>
  );
}
```

## TypeScript Integration

### 1. Typed Variants

```tsx
import { motion, Variants } from 'framer-motion';

interface AnimationProps {
  isVisible: boolean;
  children: React.ReactNode;
}

const fadeVariants: Variants = {
  hidden: {
    opacity: 0,
    y: 20,
    transition: {
      duration: 0.3
    }
  },
  visible: {
    opacity: 1,
    y: 0,
    transition: {
      duration: 0.3
    }
  }
};

export function TypedAnimation({ isVisible, children }: AnimationProps) {
  return (
    <motion.div
      variants={fadeVariants}
      initial="hidden"
      animate={isVisible ? "visible" : "hidden"}
    >
      {children}
    </motion.div>
  );
}
```

### 2. Custom Motion Components

```tsx
import { motion, HTMLMotionProps } from 'framer-motion';
import { forwardRef } from 'react';

interface CustomButtonProps extends HTMLMotionProps<"button"> {
  variant?: 'primary' | 'secondary';
  size?: 'sm' | 'md' | 'lg';
}

export const MotionButton = forwardRef<HTMLButtonElement, CustomButtonProps>(
  ({ variant = 'primary', size = 'md', children, className, ...props }, ref) => {
    const baseClasses = "font-medium rounded-lg transition-colors";
    const variantClasses = {
      primary: "bg-blue-500 hover:bg-blue-600 text-white",
      secondary: "bg-gray-200 hover:bg-gray-300 text-gray-900"
    };
    const sizeClasses = {
      sm: "px-3 py-1.5 text-sm",
      md: "px-4 py-2",
      lg: "px-6 py-3 text-lg"
    };

    return (
      <motion.button
        ref={ref}
        className={`${baseClasses} ${variantClasses[variant]} ${sizeClasses[size]} ${className}`}
        whileHover={{ scale: 1.05 }}
        whileTap={{ scale: 0.95 }}
        {...props}
      >
        {children}
      </motion.button>
    );
  }
);

MotionButton.displayName = 'MotionButton';
```

## Best Practices

### 1. Performance Guidelines

- Use `transform` properties (x, y, scale, rotate) instead of layout properties
- Implement `will-change: transform` for draggable elements
- Use `layoutId` for shared element transitions
- Respect user motion preferences with `prefers-reduced-motion`
- Clean up animations and event listeners properly

### 2. Accessibility

```tsx
import { motion } from 'framer-motion';

// Respect reduced motion preferences
const shouldReduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

export function AccessibleComponent() {
  return (
    <motion.div
      initial={shouldReduceMotion ? {} : { opacity: 0 }}
      animate={shouldReduceMotion ? {} : { opacity: 1 }}
      transition={shouldReduceMotion ? { duration: 0 } : { duration: 0.5 }}
      // Ensure interactive elements are keyboard accessible
      tabIndex={0}
      role="button"
      aria-label="Animated button"
    >
      Content
    </motion.div>
  );
}
```

### 3. Code Organization

```tsx
// animations/variants.ts
export const fadeInUp = {
  initial: { opacity: 0, y: 20 },
  animate: { opacity: 1, y: 0 },
  exit: { opacity: 0, y: -20 }
};

export const slideInLeft = {
  initial: { opacity: 0, x: -50 },
  animate: { opacity: 1, x: 0 },
  exit: { opacity: 0, x: 50 }
};

// components/AnimatedWrapper.tsx
import { motion } from 'framer-motion';
import { fadeInUp } from '../animations/variants';

interface AnimatedWrapperProps {
  children: React.ReactNode;
  delay?: number;
}

export function AnimatedWrapper({ children, delay = 0 }: AnimatedWrapperProps) {
  return (
    <motion.div
      variants={fadeInUp}
      initial="initial"
      animate="animate"
      exit="exit"
      transition={{ delay }}
    >
      {children}
    </motion.div>
  );
}
```

## Troubleshooting Common Issues

### 1. Layout Thrashing

```tsx
// ❌ Bad - causes layout thrashing
<motion.div animate={{ width: 200, height: 200 }} />

// ✅ Good - uses transform
<motion.div animate={{ scale: 1.5 }} />
```

### 2. Memory Leaks

```tsx
import { useEffect } from 'react';
import { useAnimation } from 'framer-motion';

export function ProperCleanup() {
  const controls = useAnimation();

  useEffect(() => {
    const animationPromise = controls.start({ x: 100 });
    
    return () => {
      // Cancel ongoing animations
      animationPromise.then(animation => animation?.stop());
    };
  }, [controls]);

  return <motion.div animate={controls} />;
}
```

### 3. Hydration Issues (Next.js)

```tsx
import { motion } from 'framer-motion';
import { useEffect, useState } from 'react';

export function HydrationSafeComponent() {
  const [isClient, setIsClient] = useState(false);

  useEffect(() => {
    setIsClient(true);
  }, []);

  if (!isClient) {
    return <div>Loading...</div>;
  }

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
    >
      Content
    </motion.div>
  );
}
```

## Resources

- [Framer Motion Documentation](https://www.framer.com/motion/)
- [Framer Motion API Reference](https://www.framer.com/motion/api/)
- [Motion Examples](https://codesandbox.io/examples/package/framer-motion)
- [React Spring vs Framer Motion](https://blog.logrocket.com/react-spring-vs-framer-motion/)
- [Animation Performance](https://web.dev/animations/)