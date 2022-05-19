import { Link } from "solid-app-router";
import styles from "../App.module.css";

const Another = () => {
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
