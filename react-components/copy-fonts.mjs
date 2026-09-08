// Copy the self-hosted Roboto (@fontsource/roboto) into the served assets,
// mirroring trame-vuetify's bundled roboto/ directory.
import { cpSync, mkdirSync, rmSync } from "node:fs";
import { createRequire } from "node:module";
import { dirname, join } from "node:path";

const require = createRequire(import.meta.url);
const src = dirname(require.resolve("@fontsource/roboto/400.css"));
const dst = "../src/trame_mui/module/serve/roboto";

rmSync(dst, { recursive: true, force: true });
mkdirSync(join(dst, "files"), { recursive: true });
for (const weight of [300, 400, 500, 700]) {
  cpSync(join(src, `${weight}.css`), join(dst, `${weight}.css`));
}
cpSync(join(src, "files"), join(dst, "files"), {
  recursive: true,
  filter: (f) => !f.includes("italic"),
});
console.log("Roboto copied to", dst);
