# Thread Safety

- Synchronization primitives:
  - `System.Threading.Barrier`
  - `System.Threading.ReaderWriterLockSlim` (prefered)
  - `System.Threading.ReaderWriterLock`
  - `System.Threading.SemaphoreSlim` (prefered)
  - `System.Threading.Semaphore`
  - `System.Threading.AsyncLocal<T>`
- Concurrent data structures
  - `System.Collections.Concurrent.*`
