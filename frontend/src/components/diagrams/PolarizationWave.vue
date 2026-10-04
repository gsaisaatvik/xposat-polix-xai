<template>
  <svg class="diagram-svg" viewBox="0 0 640 220" role="img" aria-label="Animated transverse wave with a highlighted oscillation plane">
    <text x="16" y="28" class="diagram-label">Travel direction</text>
    <line x1="20" y1="110" x2="620" y2="110" class="axis" />
    <polygon points="620,110 604,102 604,118" class="axis-head" />
    <path class="wave-glow" d="M40 110 C90 30 140 190 190 110 S290 30 340 110 S440 190 490 110 S590 30 620 110" />
    <path class="wave-line" d="M40 110 C90 30 140 190 190 110 S290 30 340 110 S440 190 490 110 S590 30 620 110" />
    <g class="plane-marker">
      <line x1="190" y1="40" x2="190" y2="180" />
      <circle cx="190" cy="48" r="6" />
    </g>
    <text x="210" y="52" class="diagram-label">Oscillation plane</text>
  </svg>
</template>
