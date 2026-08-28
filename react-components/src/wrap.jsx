
// Generic MUI wrapper honoring the trame contract:
// - children arrive through the scoped-slot render prop `slot`
// - r_model arrives as `value` + `onUpdateValue(newValue)` and is mapped to
//   the component's controlled prop/event through its model config
export default function wrap(Component, name, model) {
  function Wrapped({ slot, value, onUpdateValue, ...props }) {
    const finalProps = { ...props };
    if (model && onUpdateValue) {
      finalProps[model.prop] = value ?? finalProps[model.prop];
      const userHandler = props[model.event];
      finalProps[model.event] = (...args) => {
        onUpdateValue(model.extract(...args));
        userHandler?.(...args);
      };
    } else if (value !== undefined) {
      finalProps.value = value;
    }
    const children = slot ? slot() : null;
    if (children === null || (Array.isArray(children) && !children.length)) {
      return <Component {...finalProps} />;
    }
    return <Component {...finalProps}>{children}</Component>;
  }
  Wrapped.displayName = `Trame${name}`;
  return Wrapped;
}
