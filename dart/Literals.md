# Array Literals

```dart
List<Object> objects = [
  "",
  17,
  Person()
];

List<Person> people = <Person>[
  Person(),
  Person()
];
```

- List literals are of type `List<T>`
- To improve type inference and restrict the type of array elements, place
  `<Person>` before `[]`
  ```dart
  // List<Person>
  var people = <Person>[
    Person(),
    Person()
    // place int here would trigger compiler error
  ];
  ```
