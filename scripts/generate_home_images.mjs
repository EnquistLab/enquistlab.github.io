import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { execFileSync } from "node:child_process";
import { mkdirSync, readFileSync, statSync } from "node:fs";
import { fileURLToPath } from "node:url";

const root = fileURLToPath(new URL("../", import.meta.url));
const images = [
  ["field/field_opening.jpeg", [640, 960, 1440, 1920, 2560]],
  ["field/brian_field.jpg", [320, 640, 800]],
  ["field/aberg_andes.jpeg", [320, 640, 960]],
  ["field/pftc_peru_students.jpeg", [320, 640, 960]],
  ["field/rmbl_alpine.jpg", [320, 640, 960]],
  ["field/sefdp_lidar.jpg", [320, 640, 960]],
  ["wordpress/dsc_3414.jpeg", [320, 640, 960]],
];
const checkOnly = process.argv.includes("--check");
const checksum = (path) => createHash("sha256").update(readFileSync(path)).digest("hex");
const dimensions = (path) => {
  const output = execFileSync("sips", ["-g", "pixelWidth", "-g", "pixelHeight", path], { encoding: "utf8" });
  return [Number(output.match(/pixelWidth: (\d+)/)[1]), Number(output.match(/pixelHeight: (\d+)/)[1])];
};
let originalBytes = 0;
let largestCandidateBytes = 0;
mkdirSync(`${root}assets/img/home`, { recursive: true });
for (const [source, widths] of images) {
  const original = `${root}assets/img/${source}`;
  const before = checksum(original);
  const [originalWidth, originalHeight] = dimensions(original);
  const name = source
    .split("/")
    .pop()
    .replace(/\.[^.]+$/, "");
  originalBytes += statSync(original).size;
  for (const width of widths) {
    assert.ok(width <= originalWidth, `${source}: no upscaling`);
    const output = `${root}assets/img/home/${name}-${width}.jpg`;
    if (!checkOnly) {
      execFileSync("sips", ["-s", "format", "jpeg", "-s", "formatOptions", "78", "--resampleWidth", String(width), original, "--out", output]);
    }
    const [actualWidth, actualHeight] = dimensions(output);
    assert.equal(actualWidth, width, output);
    assert.ok(Math.abs(actualHeight - (originalHeight * width) / originalWidth) <= 1, `${output}: aspect ratio`);
    if (width === widths.at(-1)) largestCandidateBytes += statSync(output).size;
  }
  assert.equal(checksum(original), before, `${source}: original preserved`);
  console.log(`SHA256 ${before}  assets/img/${source}`);
}
console.log(
  `PASS: 7 originals preserved; 23 derivative dimensions verified. Original bytes: ${originalBytes}; largest candidates combined: ${largestCandidateBytes}.`
);
