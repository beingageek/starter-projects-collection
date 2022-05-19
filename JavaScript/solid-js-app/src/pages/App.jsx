import { Link } from "solid-app-router";
import styles from "../App.module.css";

const App = () => {
  return (
    <div class={styles.App}>
      <header class={styles.header}>
        Home
        <Link href="/another">
          <a>Go to Another</a>
        </Link>
        <Link href="/solid">
          <a>About</a>
        </Link>
      </header>
    </div>
  );
};

export default App;
