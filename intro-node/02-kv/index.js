import * as pebl from "pebl";

console.log(await pebl.get("foo"));
await pebl.set("foo", "bar");
console.log(await pebl.get("foo"));
