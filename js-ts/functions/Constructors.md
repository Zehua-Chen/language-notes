# Constructors

Constructors are special functions in JavaScript that constructs objects.

In an object,

- The object's `constructor` property points to the function
- The constructor is contained in the prototype

## Prototype Ovewritten

If the prototype of an object is explicitly specified

```js
function T() {}

T.prototype = {};
```

Then the above notes about constructors would no longer be valid
