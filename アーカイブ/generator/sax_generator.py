from generator.melody_generator import MelodyGenerator


class SaxGenerator(MelodyGenerator):
    def __init__(self, **kwargs):
        # デフォルトで Alto Saxophone を指定（必要に応じて main_cfg で上書き可）
        super().__init__(instrument_name="Alto Saxophone", **kwargs)

    def apply_humanize(self, part):
        profile_name = (
            self.cfg.get("humanize_profile")
            or section_data.get("humanize_profile")
            or self.global_settings.get("humanize_profile")
        )
        if profile_name:
            humanizer.apply(part, profile_name)

        # スコア全体
        if global_profile:
            humanizer.apply(score, global_profile)
