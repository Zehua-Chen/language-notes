# Required Initializers

- When the class has `open` accessibility, the required initializers must be
  `public`

  ```swift
  open class Foo {
    public required init() {
      print(#function)
    }
  }

  open class Boo: Foo {
    public required init() {
      print(#function)
    }
  }
  ```

- Every subclass has to implement the required initializer of the base class
- Required initializer enable instantiations using meta classes
  ```swift
  let subclass = Foo.self.init()
  ```
