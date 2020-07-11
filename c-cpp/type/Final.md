# Final Class/Struct

```cpp
struct Parent {
  virtual void foo() {
    cout << "parent" << endl;
  }
};

struct Child final: public Parent {
  void foo () override {
    this->Parent::foo();
    cout << "child" << endl;
  }
};

```

Note that `final` comes after `Child`

## Performance Benefits

Final allows compiler to perform devirtualization, i.e. not using vtable to
invoke virtual method, providing performance benefits (Source:
[The Performance Benefits of Final Classes](https://devblogs.microsoft.com/cppblog/the-performance-benefits-of-final-classes/))
