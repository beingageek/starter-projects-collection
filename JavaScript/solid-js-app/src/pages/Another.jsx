import { A as Link } from "@solidjs/router";
import styles from "../App.module.css";

function Another() {
  return (
    <div class={styles.App}>
      <header class={styles.header}>
        <h1>Another page</h1>
        <Link href="/">
          <a>Back</a>
        </Link>
      </header>
    </div>
  );
};

export default Another;
