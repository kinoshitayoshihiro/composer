# Arrangement Features

This document outlines several rhythm and arrangement options available in the project.

## `mirror_melody` for Bass Parts

The bass generator can optionally mirror the main melody line. When `mirror_melody: true` is set in the bass part parameters, the bass line is generated by inverting the melody around the tonic pitch. This creates a contrapuntal effect where the bass moves opposite to the melody.

Typical usage in a part configuration:

```yaml
bass_part:
  pattern_key: walking_8ths
  mirror_melody: true
```

If disabled or omitted, the bass follows its normal pattern selection based on emotion buckets and intensity.

## `guitar_emotion_arpeggio` Rhythm Key

The rhythm library includes a pattern named `guitar_emotion_arpeggio`. It selects arpeggio note ordering depending on the current emotion bucket. Each bucket (e.g., `calm`, `groovy`, `energetic`) maps to a different set of arpeggio indices, giving subtly different movement for gentle versus intense passages.

The guitar generator resolves the rhythm key using the emotion bucket determined from the section's `musical_intent`. For example, a `calm` bucket might produce a slow ascending arpeggio, while an `energetic` bucket chooses a wider, faster pattern.

The mapping is defined in the YAML rhythm library. When a section specifies `rhythm_key: guitar_emotion_arpeggio`, the generator looks up the appropriate arpeggio indices according to its bucket and intensity before rendering the notes.
