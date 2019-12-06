# Event Loop

- JavaScript VM maintains a "callback queue", while using async APIs, the
  callback would be added to the queue when the async tasks completes.
- When the tasks at hand is done, the VM would get more tasks from the
  callback queue

## Micro and Macro Tasks

When the VM looks for more tasks, it would execute **micro tasks** first,
and then **macro tasks**

Macro tasks:

- `setTimeout`
- `setInterval`
- `setImmediate`

Micro tasks:

- `Promise`
- `process.nextTick`
