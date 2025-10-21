"""
## 1. Document Layer Management System

**Problem**: Implement a document management system that supports applying properties to layers with undo/redo functionality.

**Part A**: Basic Implementation
Create a `Document` class with the following methods:
- `__init__()`: Initialize the document system
- `apply(layer_id, property_name, value)`: Apply a property value to a specific layer
- `undo()`: Undo the most recent operation

**Part B**: Batch Operations
- `commit_batch()`: Commit a batch of operations as a single unit
- Update `undo()` to handle undoing entire batches

**Part C**: Redo Functionality
- Implement `redo()` method to reapply undone operations

**Example**:
```python
doc = Document()
doc.apply(1, "color", "green")       # Layer 1: {color: green}
doc.apply(2, "shape", "triangle")    # Layer 2: {shape: triangle}
doc.apply(1, "color", "blue")        # Layer 1: {color: blue}
doc.undo()                           # Layer 1: {color: green}
```

**Follow-up**: How would you optimize memory usage when dealing with 10,000+ layers?
"""
   

class Document:
    def __init__(self):
        # Stores layer_id -> {property_name: value}
        self.layers = {}
        # Undo/redo stacks
        self.undo_stack = []
        self.redo_stack = []

    def apply(self, layer_id, property_name, value):
        """Apply a property value to a specific layer"""
        # Ensure the layer
        if layer_id not in self.layers:
            self.layers[layer_id] = {}

        # Save old value (may be None if property not set yet)
        old_value = self.layers[layer_id].get(property_name)

        # Apply new value
        self.layers[layer_id][property_name] = value

        # Record operation for undo
        self.undo_stack.append((layer_id, property_name, old_value, value))
        self.redo_stack.clear()  # clear redo history on new action

    def undo(self):
        """Undo the most recent operation"""
        if not self.undo_stack:
            print("Nothing to undo")
            return

        layer_id, property_name, old_value, new_value = self.undo_stack.pop()

        # Restore old value
        if old_value is None:
            # Property didn’t exist before → delete it
            self.layers[layer_id].pop(property_name, None)
        else:
            self.layers[layer_id][property_name] = old_value

        # Save to redo stack
        self.redo_stack.append((layer_id, property_name, old_value, new_value))

    def redo(self):
        """Redo the most recently undone operation"""
        if not self.redo_stack:
            print("Nothing to redo")
            return

        layer_id, property_name, old_value, new_value = self.redo_stack.pop()

        # Reapply new value
        self.layers[layer_id][property_name] = new_value

        # Push back into undo stack
        self.undo_stack.append((layer_id, property_name, old_value, new_value))

    def __repr__(self):
        return f"Document(layers={self.layers})"


### test
'''python
doc = Document()
doc.apply(1, "color", "green")       # Layer 1: {color: green}
doc.apply(2, "shape", "triangle")    # Layer 2: {shape: triangle}
doc.apply(1, "color", "blue")        # Layer 1: {color: blue}
doc.undo()                           # Layer 1: {color: green}
'''
if __name__ == "__main__":
    doc = Document()

    doc.apply("layer1", "color", "red")
    doc.apply("layer2", "opacity", 0.8)
    print(doc)  
    # Document(layers={'layer1': {'color': 'red', 'opacity': 0.8}})

    doc.undo()
    print(doc)
    # Document(layers={'layer1': {'color': 'red'}})

    doc.redo()
    print(doc)
    # Document(layers={'layer1': {'color': 'red', 'opacity': 0.8}})