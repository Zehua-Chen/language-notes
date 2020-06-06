# Property Wrappers

- Types that are marked with `@propertyWrapper` become property wrappers
- To access a property wrapper of a property, add a `_` prefix before the name
  of the property

# Required Implementations

- A property named `wrappedValue`, which is the property that is actually
  accessed when the user access the property marked by a property wrapper
  - Must be internal or public

# Optional Implementations

- A initializer with the signature resembling `init(wrappedValue:, ...)`:

  - The initializer can take any number of arguments after the first label
  - If the initializer only takes one parameter, then the enclosing type's
    synthesized initializer would be as if there is no property wrapper

    ```swift
    import SwiftUI

    struct Foo: View {
      // One of State's initializer is init(wrappedValue:)
      @State
      var name: String
    }

    let foo = Foo(name: "")
    ```

  - Must be internal or public

- A property named `projectedValue`; this property is accessed when the user put
  `$` operator before the property marked with the property wrapper Don’t have
  to be of the same type as the wrapped value
