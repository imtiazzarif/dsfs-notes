# Contributing

Want to add to dsfs-notes? Pull requests are welcome.

## Block format

Each block is one markdown cell plus one code cell:

```markdown
### Block N: Short title
One or two sentences on what it does and why it matters.
```

Then a code cell that:
- runs top to bottom on a fresh kernel
- has imports at the top
- has short comments explaining *why*
- prints a few results

## Rules

- Write notes in your own words. 
- No NumPy or pandas unless the book uses them.
- Keep outputs small (print every 50th or 100th step in long loops).

## Pull request

1. Fork the repo and add your block at the **end** of the notebook.
2. Restart the kernel and run all cells.
3. Open a PR with one block per PR and the book chapter it comes from.
