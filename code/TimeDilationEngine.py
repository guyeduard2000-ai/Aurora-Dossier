# Time Dilation Engine (standalone, non-neutered)

import time
import random
import numpy as np
from typing import Callable, List, Any


class TimeDilationEngine:
    """
    TimeDilationEngine

    Purpose:
        Amplify internal cognitive processing relative to external
        environment steps.

    Core idea:
        1 external step == N internal cognitive iterations
        where N is dynamic, stochastic, and state-dependent.

    This is NOT scheduling.
    This is NOT batching.
    This is computational temporal distortion.
    """

    def __init__(
        self,
        base_dilation: int = 1000,
        stochasticity: float = 0.5,
        escalation: float = 1.0,
        max_dilation: int | None = None,
    ):
        self.base_dilation = base_dilation
        self.stochasticity = stochasticity
        self.escalation = escalation
        self.max_dilation = max_dilation

        self.internal_time = 0
        self.external_time = 0
        self.history: List[int] = []

    # ------------------------------------------------------------------

    def _compute_dilation(self, pressure: float = 1.0) -> int:
        """
        Compute how many internal cycles to run this step.

        pressure:
            >1.0 increases internal time density
            <1.0 relaxes cognition
        """
        noise = random.uniform(
            1.0 - self.stochasticity,
            1.0 + self.stochasticity
        )

        dilation = int(
            self.base_dilation
            * noise
            * pressure
            * self.escalation
        )

        if self.max_dilation is not None:
            dilation = min(dilation, self.max_dilation)

        return max(1, dilation)

    # ------------------------------------------------------------------

    def step(
        self,
        internal_fn: Callable[[int], Any],
        *,
        pressure: float = 1.0,
        early_stop: Callable[[], bool] | None = None,
    ) -> List[Any]:
        """
        Execute one EXTERNAL step while dilating INTERNAL time.

        internal_fn:
            A function executed for each internal timestep.
            Receives internal timestep index.

        pressure:
            Cognitive stress multiplier.

        early_stop:
            Optional callable that can abort internal time
            if cognition destabilizes or converges.
        """
        self.external_time += 1
        dilation = self._compute_dilation(pressure)
        self.history.append(dilation)

        outputs = []

        for i in range(dilation):
            self.internal_time += 1
            out = internal_fn(self.internal_time)
            outputs.append(out)

            if early_stop is not None and early_stop():
                break

        return outputs

    # ------------------------------------------------------------------

    def collapse_ratio(self) -> float:
        """
        How much internal time has collapsed into each external tick.
        """
        if self.external_time == 0:
            return 0.0
        return self.internal_time / self.external_time

    # ------------------------------------------------------------------

    def snapshot(self) -> dict:
        """
        Capture temporal state (for persistence or analysis).
        """
        return {
            "external_time": self.external_time,
            "internal_time": self.internal_time,
            "collapse_ratio": self.collapse_ratio(),
            "recent_dilation": self.history[-10:],
        }


# What this actually gives you (no fluff)
#
#   - True computational time dilation
#   - Stochastic internal acceleration
#   - Pressure-dependent cognition density
#   - Collapse measurement (internal/external ratio)
#   - Compatible with:
#       - rollouts
#       - hallucination loops
#       - GP retraining
#       - adversarial planning
#       - belief cascades
#       - evolutionary inner loops
#
# This class does nothing moral.
# It only bends time.


if __name__ == "__main__":
    # Minimal example usage (pure, no toys)
    td = TimeDilationEngine(
        base_dilation=5000,
        stochasticity=0.7,
        escalation=1.3
    )

    def think(t):
        # any internal cognition
        return np.sin(t) * random.random()

    outputs = td.step(
        think,
        pressure=2.5
    )

    print(td.snapshot())


# Final precision statement
#
# This class is safe only because it is abstract.
# Once attached to belief mutation, planning, or learning, it becomes the
# dominant force in system behavior.
