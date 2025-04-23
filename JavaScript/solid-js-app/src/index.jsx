import { Route, Router } from "@solidjs/router";
import { lazy, Suspense } from "solid-js";
import { render } from "solid-js/web";
import "./index.css";

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

const Another = lazy(() => sleep(500).then(() => import("./pages/Another")));
const App = lazy(() => import("./pages/App"));
const SolidLogo = lazy(() => import("./pages/SolidLogo"));

render(
  () => (
    <Router>
      <Suspense fallback="Loading...">
        <Route path="/" component={App} />
        <Route path="/another" component={Another} />
        <Route path="/solid" component={SolidLogo} />
      </Suspense>
    </Router>
  ),
  document.getElementById("root")
);
