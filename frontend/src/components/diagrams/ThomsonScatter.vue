<template>
  <svg class="diagram-svg" viewBox="0 0 640 260" role="img" aria-label="Stylized Thomson scattering: incoming X-ray, scatterer, and outgoing directions">
    <text x="20" y="28" class="diagram-label">Incoming X-ray</text>
    <path class="in-beam" d="M30 130 H250" />
    <circle class="scatterer" cx="310" cy="130" r="18" />
    <text x="292" y="176" class="diagram-label">Electron</text>
    <g class="out-beams">
      <path d="M328 118 L520 48" />
      <path d="M328 142 L520 212" />
      <path class="preferred" d="M328 130 L560 130" />
    </g>
    <text x="430" y="40" class="diagram-label">Scattered directions</text>
    <text x="430" y="124" class="diagram-label preferred-label">Preferred plane remains</text>
  </svg>
</template>
