# React TypeScript - Modern Patterns & Best Practices (2025)

React TypeScript development has evolved significantly with React 18+, TypeScript 5.0+, and modern tooling. This guide covers the latest patterns, best practices, and advanced techniques for building robust React applications.

## Setup & Configuration

### 1. Modern Project Setup

```bash
# Create new project with TypeScript
npx create-next-app@latest my-app --typescript --tailwind --eslint --app

# Or with Vite
npm create vite@latest my-app -- --template react-ts

# Add essential dependencies
npm install @types/react @types/react-dom @types/node
```

### 2. TypeScript Configuration

```json
// tsconfig.json
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["DOM", "DOM.Iterable", "ES2022"],
    "module": "ESNext",
    "moduleResolution": "bundler",
    "allowJs": true,
    "checkJs": false,
    "jsx": "preserve",
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "outDir": "./dist",
    "removeComments": true,
    "noEmit": true,
    "isolatedModules": true,
    "allowSyntheticDefaultImports": true,
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "skipLibCheck": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"],
      "@/components/*": ["./src/components/*"],
      "@/lib/*": ["./src/lib/*"],
      "@/types/*": ["./src/types/*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx"],
  "exclude": ["node_modules"]
}
```

## Modern Component Patterns

### 1. Function Components with TypeScript

```tsx
import { ReactNode, ComponentProps } from 'react';

// Basic component with props
interface ButtonProps {
  children: ReactNode;
  variant?: 'primary' | 'secondary' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  onClick?: () => void;
}

export function Button({ 
  children, 
  variant = 'primary', 
  size = 'md', 
  disabled = false,
  onClick,
  ...props 
}: ButtonProps) {
  return (
    <button
      className={`btn btn-${variant} btn-${size}`}
      disabled={disabled}
      onClick={onClick}
      {...props}
    >
      {children}
    </button>
  );
}

// Extending native element props
interface CustomInputProps extends ComponentProps<'input'> {
  label?: string;
  error?: string;
}

export function CustomInput({ label, error, className, ...props }: CustomInputProps) {
  return (
    <div className="form-group">
      {label && <label className="form-label">{label}</label>}
      <input 
        className={`form-input ${error ? 'error' : ''} ${className}`}
        {...props}
      />
      {error && <span className="error-message">{error}</span>}
    </div>
  );
}
```

### 2. Generic Components

```tsx
import { ReactNode } from 'react';

// Generic list component
interface ListProps<T> {
  items: T[];
  renderItem: (item: T, index: number) => ReactNode;
  keyExtractor: (item: T, index: number) => string | number;
  className?: string;
}

export function List<T>({ 
  items, 
  renderItem, 
  keyExtractor, 
  className 
}: ListProps<T>) {
  return (
    <ul className={className}>
      {items.map((item, index) => (
        <li key={keyExtractor(item, index)}>
          {renderItem(item, index)}
        </li>
      ))}
    </ul>
  );
}

// Usage
interface User {
  id: number;
  name: string;
  email: string;
}

function UserList({ users }: { users: User[] }) {
  return (
    <List
      items={users}
      keyExtractor={user => user.id}
      renderItem={user => (
        <div>
          <h3>{user.name}</h3>
          <p>{user.email}</p>
        </div>
      )}
    />
  );
}
```

### 3. Compound Components

```tsx
import { ReactNode, createContext, useContext } from 'react';

// Context for compound component
interface CardContextType {
  variant: 'default' | 'elevated' | 'outlined';
}

const CardContext = createContext<CardContextType | null>(null);

// Main component
interface CardProps {
  children: ReactNode;
  variant?: CardContextType['variant'];
  className?: string;
}

function Card({ children, variant = 'default', className }: CardProps) {
  return (
    <CardContext.Provider value={{ variant }}>
      <div className={`card card-${variant} ${className}`}>
        {children}
      </div>
    </CardContext.Provider>
  );
}

// Sub-components
function CardHeader({ children, className }: { children: ReactNode; className?: string }) {
  const context = useContext(CardContext);
  if (!context) throw new Error('CardHeader must be used within Card');
  
  return (
    <div className={`card-header ${className}`}>
      {children}
    </div>
  );
}

function CardContent({ children, className }: { children: ReactNode; className?: string }) {
  return (
    <div className={`card-content ${className}`}>
      {children}
    </div>
  );
}

function CardFooter({ children, className }: { children: ReactNode; className?: string }) {
  return (
    <div className={`card-footer ${className}`}>
      {children}
    </div>
  );
}

// Compound component pattern
Card.Header = CardHeader;
Card.Content = CardContent;
Card.Footer = CardFooter;

export { Card };

// Usage
function App() {
  return (
    <Card variant="elevated">
      <Card.Header>
        <h2>Card Title</h2>
      </Card.Header>
      <Card.Content>
        <p>Card content goes here</p>
      </Card.Content>
      <Card.Footer>
        <Button>Action</Button>
      </Card.Footer>
    </Card>
  );
}
```

## Modern Hooks Patterns

### 1. Custom Hooks with TypeScript

```tsx
import { useState, useEffect, useCallback, useRef } from 'react';

// Fetch hook with proper typing
interface UseFetchResult<T> {
  data: T | null;
  loading: boolean;
  error: Error | null;
  refetch: () => void;
}

function useFetch<T>(url: string): UseFetchResult<T> {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);
  const abortControllerRef = useRef<AbortController | null>(null);

  const fetchData = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);
      
      // Cancel previous request
      if (abortControllerRef.current) {
        abortControllerRef.current.abort();
      }
      
      abortControllerRef.current = new AbortController();
      
      const response = await fetch(url, {
        signal: abortControllerRef.current.signal,
      });
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const result = await response.json();
      setData(result);
    } catch (err) {
      if (err instanceof Error && err.name !== 'AbortError') {
        setError(err);
      }
    } finally {
      setLoading(false);
    }
  }, [url]);

  useEffect(() => {
    fetchData();
    
    return () => {
      if (abortControllerRef.current) {
        abortControllerRef.current.abort();
      }
    };
  }, [fetchData]);

  return { data, loading, error, refetch: fetchData };
}

// Local storage hook
function useLocalStorage<T>(key: string, initialValue: T) {
  const [storedValue, setStoredValue] = useState<T>(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error(`Error reading localStorage key "${key}":`, error);
      return initialValue;
    }
  });

  const setValue = useCallback((value: T | ((val: T) => T)) => {
    try {
      const valueToStore = value instanceof Function ? value(storedValue) : value;
      setStoredValue(valueToStore);
      window.localStorage.setItem(key, JSON.stringify(valueToStore));
    } catch (error) {
      console.error(`Error setting localStorage key "${key}":`, error);
    }
  }, [key, storedValue]);

  return [storedValue, setValue] as const;
}

// Debounce hook
function useDebounce<T>(value: T, delay: number): T {
  const [debouncedValue, setDebouncedValue] = useState<T>(value);

  useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => {
      clearTimeout(handler);
    };
  }, [value, delay]);

  return debouncedValue;
}
```

### 2. Advanced State Management

```tsx
import { useReducer, useCallback, useContext, createContext, ReactNode } from 'react';

// State management with useReducer
interface User {
  id: string;
  name: string;
  email: string;
}

interface UserState {
  users: User[];
  loading: boolean;
  error: string | null;
}

type UserAction =
  | { type: 'FETCH_START' }
  | { type: 'FETCH_SUCCESS'; payload: User[] }
  | { type: 'FETCH_ERROR'; payload: string }
  | { type: 'ADD_USER'; payload: User }
  | { type: 'UPDATE_USER'; payload: { id: string; updates: Partial<User> } }
  | { type: 'DELETE_USER'; payload: string };

function userReducer(state: UserState, action: UserAction): UserState {
  switch (action.type) {
    case 'FETCH_START':
      return { ...state, loading: true, error: null };
    case 'FETCH_SUCCESS':
      return { ...state, loading: false, users: action.payload };
    case 'FETCH_ERROR':
      return { ...state, loading: false, error: action.payload };
    case 'ADD_USER':
      return { ...state, users: [...state.users, action.payload] };
    case 'UPDATE_USER':
      return {
        ...state,
        users: state.users.map(user =>
          user.id === action.payload.id
            ? { ...user, ...action.payload.updates }
            : user
        ),
      };
    case 'DELETE_USER':
      return {
        ...state,
        users: state.users.filter(user => user.id !== action.payload),
      };
    default:
      return state;
  }
}

// Context for state management
interface UserContextType {
  state: UserState;
  actions: {
    fetchUsers: () => Promise<void>;
    addUser: (user: Omit<User, 'id'>) => void;
    updateUser: (id: string, updates: Partial<User>) => void;
    deleteUser: (id: string) => void;
  };
}

const UserContext = createContext<UserContextType | null>(null);

export function UserProvider({ children }: { children: ReactNode }) {
  const [state, dispatch] = useReducer(userReducer, {
    users: [],
    loading: false,
    error: null,
  });

  const actions = {
    fetchUsers: useCallback(async () => {
      dispatch({ type: 'FETCH_START' });
      try {
        const response = await fetch('/api/users');
        const users = await response.json();
        dispatch({ type: 'FETCH_SUCCESS', payload: users });
      } catch (error) {
        dispatch({ 
          type: 'FETCH_ERROR', 
          payload: error instanceof Error ? error.message : 'Unknown error' 
        });
      }
    }, []),

    addUser: useCallback((userData: Omit<User, 'id'>) => {
      const newUser: User = {
        id: Date.now().toString(),
        ...userData,
      };
      dispatch({ type: 'ADD_USER', payload: newUser });
    }, []),

    updateUser: useCallback((id: string, updates: Partial<User>) => {
      dispatch({ type: 'UPDATE_USER', payload: { id, updates } });
    }, []),

    deleteUser: useCallback((id: string) => {
      dispatch({ type: 'DELETE_USER', payload: id });
    }, []),
  };

  return (
    <UserContext.Provider value={{ state, actions }}>
      {children}
    </UserContext.Provider>
  );
}

export function useUsers() {
  const context = useContext(UserContext);
  if (!context) {
    throw new Error('useUsers must be used within UserProvider');
  }
  return context;
}
```

## Advanced Type Patterns

### 1. Utility Types

```tsx
// Utility types for better type safety
type Optional<T, K extends keyof T> = Omit<T, K> & Partial<Pick<T, K>>;
type Required<T, K extends keyof T> = T & Required<Pick<T, K>>;

// Example usage
interface User {
  id: string;
  name: string;
  email: string;
  avatar?: string;
}

// Make avatar required
type UserWithAvatar = Required<User, 'avatar'>;

// Make email optional
type UserDraft = Optional<User, 'email'>;

// Conditional types
type NonNullable<T> = T extends null | undefined ? never : T;

// Template literal types
type EventName = `on${Capitalize<string>}`;
type ButtonEvent = `button${Capitalize<string>}`;

// Mapped types
type EventHandlers<T> = {
  [K in keyof T as `on${Capitalize<string & K>}`]: (value: T[K]) => void;
};

interface FormData {
  name: string;
  email: string;
  age: number;
}

type FormEventHandlers = EventHandlers<FormData>;
// Result: { onName: (value: string) => void; onEmail: (value: string) => void; onAge: (value: number) => void; }
```

### 2. Discriminated Unions

```tsx
// API response patterns
interface LoadingState {
  status: 'loading';
}

interface SuccessState {
  status: 'success';
  data: any;
}

interface ErrorState {
  status: 'error';
  error: string;
}

type AsyncState = LoadingState | SuccessState | ErrorState;

function AsyncComponent({ state }: { state: AsyncState }) {
  switch (state.status) {
    case 'loading':
      return <div>Loading...</div>;
    case 'success':
      return <div>Data: {JSON.stringify(state.data)}</div>;
    case 'error':
      return <div>Error: {state.error}</div>;
    default:
      // TypeScript ensures exhaustive checking
      const _exhaustive: never = state;
      return _exhaustive;
  }
}

// Form field types
interface TextFieldProps {
  type: 'text';
  placeholder?: string;
}

interface NumberFieldProps {
  type: 'number';
  min?: number;
  max?: number;
}

interface SelectFieldProps {
  type: 'select';
  options: Array<{ label: string; value: string }>;
}

type FieldProps = TextFieldProps | NumberFieldProps | SelectFieldProps;

function FormField(props: FieldProps & { name: string; label: string }) {
  switch (props.type) {
    case 'text':
      return (
        <input
          type="text"
          name={props.name}
          placeholder={props.placeholder}
          aria-label={props.label}
        />
      );
    case 'number':
      return (
        <input
          type="number"
          name={props.name}
          min={props.min}
          max={props.max}
          aria-label={props.label}
        />
      );
    case 'select':
      return (
        <select name={props.name} aria-label={props.label}>
          {props.options.map(option => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))}
        </select>
      );
  }
}
```

### 3. Higher-Order Components (HOCs)

```tsx
import { ComponentType, useEffect, useState } from 'react';

// HOC with proper typing
function withLoading<P extends object>(
  WrappedComponent: ComponentType<P>,
  loadingComponent: ComponentType = () => <div>Loading...</div>
) {
  return function WithLoadingComponent(props: P & { isLoading: boolean }) {
    const { isLoading, ...restProps } = props;
    
    if (isLoading) {
      return <>{loadingComponent({})}</>;
    }
    
    return <WrappedComponent {...(restProps as P)} />;
  };
}

// Usage
interface UserProfileProps {
  user: User;
  onEdit: () => void;
}

function UserProfile({ user, onEdit }: UserProfileProps) {
  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
      <button onClick={onEdit}>Edit</button>
    </div>
  );
}

const UserProfileWithLoading = withLoading(UserProfile);

// HOC for error boundaries
function withErrorBoundary<P extends object>(
  WrappedComponent: ComponentType<P>
) {
  return function WithErrorBoundaryComponent(props: P) {
    const [hasError, setHasError] = useState(false);
    
    useEffect(() => {
      const handleError = () => setHasError(true);
      window.addEventListener('error', handleError);
      return () => window.removeEventListener('error', handleError);
    }, []);
    
    if (hasError) {
      return <div>Something went wrong</div>;
    }
    
    return <WrappedComponent {...props} />;
  };
}
```

## Performance Optimization

### 1. Memoization Patterns

```tsx
import { memo, useMemo, useCallback, ReactNode } from 'react';

// Memoized component
interface ExpensiveComponentProps {
  data: Array<{ id: string; value: number }>;
  filter: string;
  onItemClick: (id: string) => void;
}

const ExpensiveComponent = memo(function ExpensiveComponent({
  data,
  filter,
  onItemClick,
}: ExpensiveComponentProps) {
  // Memoize expensive calculations
  const filteredData = useMemo(() => {
    return data.filter(item => 
      item.id.toLowerCase().includes(filter.toLowerCase())
    );
  }, [data, filter]);

  const totalValue = useMemo(() => {
    return filteredData.reduce((sum, item) => sum + item.value, 0);
  }, [filteredData]);

  return (
    <div>
      <h2>Total: {totalValue}</h2>
      {filteredData.map(item => (
        <div key={item.id} onClick={() => onItemClick(item.id)}>
          {item.id}: {item.value}
        </div>
      ))}
    </div>
  );
});

// Parent component with memoized callbacks
function ParentComponent() {
  const [data, setData] = useState<Array<{ id: string; value: number }>>([]);
  const [filter, setFilter] = useState('');

  const handleItemClick = useCallback((id: string) => {
    console.log('Clicked item:', id);
    // Handle click logic
  }, []);

  const handleFilterChange = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
    setFilter(e.target.value);
  }, []);

  return (
    <div>
      <input 
        type="text" 
        value={filter} 
        onChange={handleFilterChange}
        placeholder="Filter items..."
      />
      <ExpensiveComponent 
        data={data} 
        filter={filter} 
        onItemClick={handleItemClick}
      />
    </div>
  );
}
```

### 2. Lazy Loading

```tsx
import { lazy, Suspense } from 'react';

// Lazy load components
const LazyDashboard = lazy(() => import('./Dashboard'));
const LazyUserProfile = lazy(() => import('./UserProfile'));
const LazySettings = lazy(() => import('./Settings'));

// Loading component
function LoadingSpinner() {
  return (
    <div className="flex items-center justify-center p-8">
      <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-500"></div>
    </div>
  );
}

// Route-based code splitting
function App() {
  const [currentRoute, setCurrentRoute] = useState('dashboard');

  const renderRoute = () => {
    switch (currentRoute) {
      case 'dashboard':
        return <LazyDashboard />;
      case 'profile':
        return <LazyUserProfile />;
      case 'settings':
        return <LazySettings />;
      default:
        return <div>404 - Page not found</div>;
    }
  };

  return (
    <div>
      <nav>
        <button onClick={() => setCurrentRoute('dashboard')}>Dashboard</button>
        <button onClick={() => setCurrentRoute('profile')}>Profile</button>
        <button onClick={() => setCurrentRoute('settings')}>Settings</button>
      </nav>
      
      <main>
        <Suspense fallback={<LoadingSpinner />}>
          {renderRoute()}
        </Suspense>
      </main>
    </div>
  );
}
```

## Error Handling

### 1. Error Boundaries

```tsx
import { Component, ReactNode, ErrorInfo } from 'react';

interface ErrorBoundaryState {
  hasError: boolean;
  error?: Error;
  errorInfo?: ErrorInfo;
}

interface ErrorBoundaryProps {
  children: ReactNode;
  fallback?: ComponentType<{ error: Error }>;
  onError?: (error: Error, errorInfo: ErrorInfo) => void;
}

class ErrorBoundary extends Component<ErrorBoundaryProps, ErrorBoundaryState> {
  constructor(props: ErrorBoundaryProps) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error: Error): ErrorBoundaryState {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    this.setState({ errorInfo });
    this.props.onError?.(error, errorInfo);
    
    // Log to error reporting service
    console.error('Error caught by boundary:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      const FallbackComponent = this.props.fallback;
      
      if (FallbackComponent && this.state.error) {
        return <FallbackComponent error={this.state.error} />;
      }
      
      return (
        <div className="error-boundary">
          <h2>Something went wrong</h2>
          <details>
            <summary>Error details</summary>
            <pre>{this.state.error?.toString()}</pre>
            <pre>{this.state.errorInfo?.componentStack}</pre>
          </details>
        </div>
      );
    }

    return this.props.children;
  }
}

// Usage
function App() {
  return (
    <ErrorBoundary 
      fallback={({ error }) => <div>Error: {error.message}</div>}
      onError={(error, errorInfo) => {
        // Send to error reporting service
        console.error('App error:', error, errorInfo);
      }}
    >
      <MainContent />
    </ErrorBoundary>
  );
}
```

### 2. Async Error Handling

```tsx
import { useState, useCallback } from 'react';

// Custom hook for async operations
function useAsyncOperation<T, P extends any[]>() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);
  const [data, setData] = useState<T | null>(null);

  const execute = useCallback(async (asyncFn: (...args: P) => Promise<T>, ...args: P) => {
    try {
      setLoading(true);
      setError(null);
      const result = await asyncFn(...args);
      setData(result);
      return result;
    } catch (err) {
      const error = err instanceof Error ? err : new Error('Unknown error');
      setError(error);
      throw error;
    } finally {
      setLoading(false);
    }
  }, []);

  return { loading, error, data, execute };
}

// Usage in component
function DataFetcher() {
  const { loading, error, data, execute } = useAsyncOperation<User[], [string]>();

  const fetchUsers = useCallback(async (query: string) => {
    await execute(async (q: string) => {
      const response = await fetch(`/api/users?q=${q}`);
      if (!response.ok) {
        throw new Error(`Failed to fetch users: ${response.statusText}`);
      }
      return response.json();
    }, query);
  }, [execute]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div>
      <button onClick={() => fetchUsers('admin')}>
        Fetch Admin Users
      </button>
      {data && (
        <ul>
          {data.map(user => (
            <li key={user.id}>{user.name}</li>
          ))}
        </ul>
      )}
    </div>
  );
}
```

## Testing Patterns

### 1. Component Testing

```tsx
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { vi } from 'vitest';
import { UserProfile } from './UserProfile';

// Mock props
const mockUser: User = {
  id: '1',
  name: 'John Doe',
  email: 'john@example.com',
};

const mockOnEdit = vi.fn();

describe('UserProfile', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('renders user information', () => {
    render(<UserProfile user={mockUser} onEdit={mockOnEdit} />);
    
    expect(screen.getByText('John Doe')).toBeInTheDocument();
    expect(screen.getByText('john@example.com')).toBeInTheDocument();
  });

  it('calls onEdit when edit button is clicked', () => {
    render(<UserProfile user={mockUser} onEdit={mockOnEdit} />);
    
    const editButton = screen.getByRole('button', { name: /edit/i });
    fireEvent.click(editButton);
    
    expect(mockOnEdit).toHaveBeenCalledTimes(1);
  });
});

// Custom hook testing
import { renderHook, act } from '@testing-library/react';
import { useFetch } from './useFetch';

describe('useFetch', () => {
  it('fetches data successfully', async () => {
    const mockData = { id: 1, name: 'Test' };
    
    global.fetch = vi.fn().mockResolvedValue({
      ok: true,
      json: () => Promise.resolve(mockData),
    });

    const { result } = renderHook(() => useFetch<typeof mockData>('/api/test'));

    expect(result.current.loading).toBe(true);
    expect(result.current.data).toBe(null);

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
      expect(result.current.data).toEqual(mockData);
    });
  });
});
```

## Next.js Integration

### 1. App Router with TypeScript

```tsx
// app/layout.tsx
import { ReactNode } from 'react';
import { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'My App',
  description: 'Built with Next.js and TypeScript',
};

interface RootLayoutProps {
  children: ReactNode;
}

export default function RootLayout({ children }: RootLayoutProps) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

// app/users/[id]/page.tsx
interface UserPageProps {
  params: { id: string };
  searchParams: { [key: string]: string | string[] | undefined };
}

export default async function UserPage({ params, searchParams }: UserPageProps) {
  const user = await fetchUser(params.id);
  
  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
    </div>
  );
}

// Generate static params
export async function generateStaticParams(): Promise<Array<{ id: string }>> {
  const users = await fetchUsers();
  return users.map(user => ({ id: user.id }));
}
```

### 2. API Routes

```tsx
// app/api/users/route.ts
import { NextRequest, NextResponse } from 'next/server';

interface User {
  id: string;
  name: string;
  email: string;
}

export async function GET(request: NextRequest) {
  try {
    const { searchParams } = new URL(request.url);
    const query = searchParams.get('q');
    
    // Fetch users logic
    const users: User[] = await fetchUsers(query);
    
    return NextResponse.json(users);
  } catch (error) {
    return NextResponse.json(
      { error: 'Failed to fetch users' },
      { status: 500 }
    );
  }
}

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    
    // Validate request body
    const userData: Omit<User, 'id'> = {
      name: body.name,
      email: body.email,
    };
    
    const newUser = await createUser(userData);
    
    return NextResponse.json(newUser, { status: 201 });
  } catch (error) {
    return NextResponse.json(
      { error: 'Failed to create user' },
      { status: 400 }
    );
  }
}

// app/api/users/[id]/route.ts
interface RouteParams {
  params: { id: string };
}

export async function GET(request: NextRequest, { params }: RouteParams) {
  try {
    const user = await fetchUser(params.id);
    
    if (!user) {
      return NextResponse.json(
        { error: 'User not found' },
        { status: 404 }
      );
    }
    
    return NextResponse.json(user);
  } catch (error) {
    return NextResponse.json(
      { error: 'Failed to fetch user' },
      { status: 500 }
    );
  }
}
```

## Best Practices Summary

### 1. Type Safety
- Use strict TypeScript configuration
- Prefer interfaces over types for object shapes
- Use discriminated unions for complex state
- Leverage utility types for type transformations

### 2. Performance
- Memoize expensive calculations with useMemo
- Use useCallback for event handlers
- Implement lazy loading for large components
- Use React.memo for pure components

### 3. Error Handling
- Implement error boundaries for component trees
- Use custom hooks for async error handling
- Provide meaningful error messages
- Log errors for debugging

### 4. Code Organization
- Use compound components for related UI elements
- Create custom hooks for reusable logic
- Separate concerns with proper file structure
- Use TypeScript for better IDE support

### 5. Testing
- Write unit tests for components and hooks
- Use React Testing Library for user-centric tests
- Mock external dependencies
- Test error scenarios

## Resources

- [React TypeScript Cheatsheet](https://react-typescript-cheatsheet.netlify.app/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [React Documentation](https://react.dev/)
- [Next.js Documentation](https://nextjs.org/docs)
- [Testing Library](https://testing-library.com/docs/react-testing-library/intro/)