import { A as Link } from "@solidjs/router";
import logo from "../assets/logo.svg";
import styles from "../App.module.css";

function App() {
  return (
    <div class={styles.App}>
      <header class={styles.header}>
        <img src={logo} class={styles.logo} alt="logo" />
        <p>This web application was made with SolidJS. The theme template is based on catppuccin.</p>
        <Link href="https://github.com/solidjs/solid" target="_blank" rel="noopener noreferrer">
          <a>Learn about SolidJS at GitHub</a>
        </Link>
        <Link href="https://github.com/catppuccin/catppuccin" target="_blank" rel="noopener noreferrer">
          <a>Learn about Catppuccin at GitHub</a>
        </Link>
        <p>
          <Link href="/" rel="noopener noreferrer">
            <a>Home @ The Programming Mantis</a>
          </Link>
        </p>
      </header>
    </div>
  );
}

export default App;
