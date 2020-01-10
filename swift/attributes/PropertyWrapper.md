# Property Wrappers

- Types that are marked with `@propertyWrapper` become property wrappers
- To access a property wrapper of a property, add a `_` prefix before the name
  of the property

# Required Implementations

- A property named `wrappedValue`, which is the property that is actually
  accessed when the user access the property marked by a property wrapper
  - Must be internal or public

# Optional Implementations

- A initializer that starts with the label `initialValue`; this takes the
  initial value that the user uses to initialize the property marked by property
  wrapper
  - The initializer can take any number of arguments after this
  - Must be internal or public
- A property named `projectedValue`; this property is accessed when the user put
  `$` operator before the property marked with the property wrapper Don’t have
  to be of the same type as the wrapped value
