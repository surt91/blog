Title: inline-python
Date: 2021-05-05 20:31
Author: surt91
Category: Code
Tags: Rust, Python
Slug: inline-python
Status: published
Lang: de

Für jeden Zweck das passende Werkzeug: In meinem Alltag bedeutet das, dass ich
Simulationen in Rust schreibe und in Python visualisiere. Dank [`inline-python`](https://crates.io/crates/inline-python)
geht das sogar sehr reibungslos.

```Rust
use inline_python::python;

fn main() {
    let x: Vec<f32> = (0..628).map(|i| i as f32 / 100.).collect();
    let y: Vec<f32> = x.iter().map(|x| x.sin()).collect();

    python! {
        import numpy as np
        from matplotlib import pyplot as plt

        plt.plot('x, 'y)
        plt.show()
    }
}
```

Dieses Minimalbeispiel ist natürlich nicht nützlich, aber ich habe es bereits produktiv
genutzt, um Dynamik auf [petgraph](https://docs.rs/petgraph/) Graphen zu
simulieren und ihren Zustand per [graph-tool](https://graph-tool.skewed.de/) zu
visualisieren.

![Graph state visualized with graph-tool](/img/inlinepy_graph.png){: class="invertable"}
