export interface SourceAsset {
  src: string
  alt: string
  caption: string
  decorative?: boolean
}

export const missionAssets = {
  satellite: {
    src: '/assets/mission/satellite-illustration-v1.png',
    alt: 'Decorative illustration of a satellite against space, not an engineering drawing',
    caption: 'Original AI-generated decorative satellite illustration. This is not an engineering diagram and is not scientific evidence.',
    decorative: true,
  },
  twoPayloads: {
    src: '/assets/mission/xposat-two-payloads-source.png',
    alt: 'Official figure showing the two XPoSat payloads',
    caption: 'Source: POLIX instrument paper (Vadawale et al. / POLIX-SRK-2020). Extracted for education; labels belong to the original publication.',
  },
  polarimetry: {
    src: '/assets/mission/polarimetry-techniques-source.png',
    alt: 'Official figure comparing X-ray polarimetry techniques',
    caption: 'Source: POLIX instrument paper (POLIX-SRK-2020). Extracted educational figure showing polarimetry technique families.',
  },
  components: {
    src: '/assets/mission/polix-components-source.png',
    alt: 'Official POLIX component layout figure',
    caption: 'Source: POLIX instrument paper (POLIX-SRK-2020). Extracted educational figure of POLIX components.',
  },
  collimator: {
    src: '/assets/mission/polix-collimator-source.png',
    alt: 'Official POLIX collimator figure',
    caption: 'Source: POLIX instrument paper (POLIX-SRK-2020). Extracted educational figure of the collimator.',
  },
  detector: {
    src: '/assets/mission/polix-detector-system-source.png',
    alt: 'Official POLIX detector-system figure',
    caption: 'Source: POLIX instrument paper (POLIX-SRK-2020). Extracted educational figure of the detector system.',
  },
  labelled: {
    src: '/assets/mission/polix-instrument-labelled-source.png',
    alt: 'Labelled POLIX instrument schematic from the data-analysis guide',
    caption: 'Source: POLIX Data Analysis Guide (October 2025). Cropped labelled instrument schematic for education.',
  },
  pipeline: {
    src: '/assets/mission/polix-level2-pipeline-source.png',
    alt: 'POLIX Level-2 processing pipeline diagram',
    caption: 'Source: POLIX Data Analysis Guide (October 2025). Cropped Level-2 pipeline diagram for education.',
  },
  tree: {
    src: '/assets/mission/polix-level2-tree-source.png',
    alt: 'POLIX Level-2 product tree diagram',
    caption: 'Source: POLIX Data Analysis Guide (October 2025). Cropped Level-2 product-tree diagram for education.',
  },
  weightedRoll: {
    src: '/assets/mission/weightedroll-columns-source.png',
    alt: 'WeightedRoll column description from the data-analysis guide',
    caption: 'Source: POLIX Data Analysis Guide (October 2025). Cropped WeightedRoll column description. This product is excluded from Matrix C in this project.',
  },
} satisfies Record<string, SourceAsset>
