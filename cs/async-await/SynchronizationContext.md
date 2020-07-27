# Synchronization Context

- If `SynchronizationContext.Current` is not null, then after `await`, the rest
  of the function would be run using `context.Post(...)`
  - Set the current context using
    `SynchronizationContext.SetSynchronizationContext(context)`
- If the current context is null, the rest of the function would continue on
  whereever the `await` is run

## Environments

- GUI frameworks or Game Engines for C# typically set `Synchronization.Current`
  to a custom implementation that run `context.Post(...)` on a UI thread

## References

- [Await, SynchronizationContext, and Console Apps](https://devblogs.microsoft.com/pfxteam/await-synchronizationcontext-and-console-apps/)
- [Parallel Computing - It's All About the SynchronizationContext](https://docs.microsoft.com/en-us/archive/msdn-magazine/2011/february/msdn-magazine-parallel-computing-it-s-all-about-the-synchronizationcontext)
