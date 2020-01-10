# Modules

Multithreading requires multiple modules to work together:

- `Core Foundation` or `Foundation`
- `Dispatch`

# The Main Dispatch Queues

- The main dispatch queues is required
  - To interface with GUI
- Only the main dispatch queue requires a run loop on the main thread to work
- The main dispatch queue runs dispatch items on the main thread
- A run loop must be active on the main thread **to execute the dispatch items
  submitted to the main disaptch queue**

## Start Run Loop On the Main Thread

```swift
// call this method on the main thread
// GUI applications created with Xcode already does this on the main thread
CFRunLoopRun()
```

- `CFRunLoopRun` gets the main run loop and run it indefinitely
