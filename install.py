#!/usr/bin/env python3
"""Качает моды, шейдеры и ресурс-паки Fantasy Coop + аниме-слой."""
from __future__ import annotations

import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MODS = ROOT / "mods"
RP = ROOT / "resourcepacks"
SP = ROOT / "shaderpacks"
UA = {"User-Agent": "Mozilla/5.0 FantasyCoop/1.1"}

FILES = [
    (MODS, "sodium-neoforge-0.8.13-mc1.21.1.jar", "https://cdn.modrinth.com/data/AANobbMI/versions/uMOpc5uV/sodium-neoforge-0.8.13%2Bmc1.21.1.jar"),
    (MODS, "iris-neoforge-1.8.14-beta.1-mc1.21.1.jar", "https://cdn.modrinth.com/data/YL57xq9U/versions/KduFYu4t/iris-neoforge-1.8.14-beta.1%2Bmc1.21.1.jar"),
    (MODS, "lithium-neoforge-0.15.4-mc1.21.1.jar", "https://cdn.modrinth.com/data/gvQqBUqZ/versions/DDUrRVCA/lithium-neoforge-0.15.4%2Bmc1.21.1.jar"),
    (MODS, "modernfix-neoforge-5.27.24-mc1.21.1.jar", "https://cdn.modrinth.com/data/nmDcB62a/versions/5HLHxQ2F/modernfix-neoforge-5.27.24%2Bmc1.21.1.jar"),
    (MODS, "ImmediatelyFast-NeoForge-1.6.14-1.21.1.jar", "https://cdn.modrinth.com/data/5ZwdcRci/versions/OUpXxw4n/ImmediatelyFast-NeoForge-1.6.14%2B1.21.1.jar"),
    (MODS, "ferritecore-7.0.3-neoforge.jar", "https://cdn.modrinth.com/data/uXXizFIs/versions/x7kQWVju/ferritecore-7.0.3-neoforge.jar"),
    (MODS, "entityculling-neoforge-1.11.1-mc1.21.1.jar", "https://cdn.modrinth.com/data/NNAgCjsB/versions/RMi7ywBj/entityculling-neoforge-1.11.1-mc1.21.1.jar"),
    (MODS, "cloth-config-15.0.140-neoforge.jar", "https://cdn.modrinth.com/data/9s6osm5g/versions/izKINKFg/cloth-config-15.0.140-neoforge.jar"),
    (MODS, "architectury-13.0.11-neoforge.jar", "https://cdn.modrinth.com/data/lhGA9TYQ/versions/1IiqEQGl/architectury-13.0.11-neoforge.jar"),
    (MODS, "geckolib-neoforge-1.21.1-4.9.3.jar", "https://cdn.modrinth.com/data/8BmcQJ2H/versions/Grwn5rUB/geckolib-neoforge-1.21.1-4.9.3.jar"),
    (MODS, "curios-neoforge-9.5.1-1.21.1.jar", "https://cdn.modrinth.com/data/vvuO3ImH/versions/yohfFbgD/curios-neoforge-9.5.1%2B1.21.1.jar"),
    (MODS, "CreativeCore_NEOFORGE_v2.13.46_mc1.21.1.jar", "https://cdn.modrinth.com/data/OsZiaDHq/versions/fdEYikBb/CreativeCore_NEOFORGE_v2.13.46_mc1.21.1.jar"),
    (MODS, "player-animation-lib-forge-2.0.4-1.21.1.jar", "https://cdn.modrinth.com/data/gedNE4y2/versions/HJZB6bmA/player-animation-lib-forge-2.0.4%2B1.21.1.jar"),
    (MODS, "CustomPlayerModels-1.21-0.6.27a.jar", "https://cdn.modrinth.com/data/h1E7sQNL/versions/YXfPij2E/CustomPlayerModels-1.21-0.6.27a.jar"),
    (MODS, "emotecraft-for-MC1.21.1-2.4.12-neoforge.jar", "https://cdn.modrinth.com/data/pZ2wrerK/versions/fu6N0NgM/emotecraft-for-MC1.21.1-2.4.12-neoforge.jar"),
    (MODS, "firstperson-neoforge-2.7.2-mc1.21.1.jar", "https://cdn.modrinth.com/data/H5XMjpHi/versions/wcETD2Bu/firstperson-neoforge-2.7.2-mc1.21.1.jar"),
    (MODS, "anime_weapons-1.0.0-neoforge-1.21.1reforged.jar", "https://mediafilez.forgecdn.net/files/6990/797/anime_weapons-1.0.0-neoforge-1.21.1reforged.jar"),
    (MODS, "better_katanas-1.0.1-neoforge-1.21.1.jar", "https://mediafilez.forgecdn.net/files/5891/824/better_katanas-1.0.1-neoforge-1.21.1.jar"),
    (MODS, "FarmersDelight-1.21.1-1.3.4.jar", "https://cdn.modrinth.com/data/R2OftAxM/versions/XTVZDOol/FarmersDelight-1.21.1-1.3.4.jar"),
    (MODS, "waystones-neoforge-1.21.1-21.1.45.jar", "https://cdn.modrinth.com/data/LOpKHB2A/versions/Is55014l/waystones-neoforge-1.21.1-21.1.45.jar"),
    (MODS, "comforts-neoforge-9.0.5-1.21.1.jar", "https://cdn.modrinth.com/data/SaCpeal4/versions/3kpPjcTc/comforts-neoforge-9.0.5%2B1.21.1.jar"),
    (MODS, "bettercombat-neoforge-2.4.0-1.21.1.jar", "https://cdn.modrinth.com/data/5sy6g3kz/versions/VhIOvcXP/bettercombat-neoforge-2.4.0%2B1.21.1.jar"),
    (MODS, "Jade-1.21.1-NeoForge-15.10.6.jar", "https://cdn.modrinth.com/data/nvQzSEkH/versions/eYz2YBGT/Jade-1.21.1-NeoForge-15.10.6.jar"),
    (MODS, "xaerominimap-neoforge-1.21.1-26.5.0.jar", "https://cdn.modrinth.com/data/1bokaNcj/versions/Q1tuMQBB/xaerominimap-neoforge-1.21.1-26.5.0.jar"),
    (MODS, "xaeroworldmap-neoforge-1.21.1-1.46.0.jar", "https://cdn.modrinth.com/data/NcUtCpym/versions/9Ckiihkz/xaeroworldmap-neoforge-1.21.1-1.46.0.jar"),
    (MODS, "create-1.21.1-6.0.10.jar", "https://cdn.modrinth.com/data/LNytGWDc/versions/UjX6dr61/create-1.21.1-6.0.10.jar"),
    (MODS, "irons_spellbooks-1.21.1-3.16.3.jar", "https://cdn.modrinth.com/data/s4OWxYQQ/versions/slKLosTb/irons_spellbooks-1.21.1-3.16.3.jar"),
    (MODS, "ars_nouveau-1.21.1-5.13.1.jar", "https://cdn.modrinth.com/data/TKB6INcv/versions/qEFs5RRw/ars_nouveau-1.21.1-5.13.1.jar"),
    (MODS, "simplyswords-neoforge-1.70.2-1.21.1.jar", "https://cdn.modrinth.com/data/bK3Ubu9p/versions/nS0Yahr5/simplyswords-neoforge-1.70.2-1.21.1.jar"),
    (MODS, "supplementaries-1.21.1-3.9.9-neoforge.jar", "https://cdn.modrinth.com/data/fFEIiSDQ/versions/WrZWfRjP/supplementaries-1.21.1-3.9.9-neoforge.jar"),
    (MODS, "chipped-neoforge-1.21.1-4.0.2.jar", "https://cdn.modrinth.com/data/BAscRYKm/versions/eqVowbGc/chipped-neoforge-1.21.1-4.0.2.jar"),
    (MODS, "aether-1.21.1-1.5.10-neoforge.jar", "https://cdn.modrinth.com/data/YhmgMVyu/versions/K5X5qMwG/aether-1.21.1-1.5.10-neoforge.jar"),
    (MODS, "deep_aether-1.21.1-1.1.5.1.jar", "https://cdn.modrinth.com/data/gcHIih5B/versions/MSW5emg8/deep_aether-1.21.1-1.1.5.1.jar"),
    (MODS, "twilightforest-1.21.1-4.8.3345-universal.jar", "https://mediafilez.forgecdn.net/files/7797/302/twilightforest-1.21.1-4.8.3345-universal.jar"),
    (MODS, "iceandfire-2.1.3.jar", "https://mediafilez.forgecdn.net/files/8929/517/iceandfire-2.1.3.jar"),
    (MODS, "mowziesmobs-1.21.1-1.8.2.jar", "https://mediafilez.forgecdn.net/files/7760/267/mowziesmobs-1.21.1-1.8.2.jar"),
    (MODS, "alexsmobs-1.22.17.jar", "https://cdn.modrinth.com/data/EmNhnNnt/versions/KSgki4uc/alexsmobs-1.22.17.jar"),
    (MODS, "BiomesOPlenty-neoforge-1.21.1-21.1.0.14.jar", "https://cdn.modrinth.com/data/HXF82T3G/versions/BtZKRp69/BiomesOPlenty-neoforge-1.21.1-21.1.0.14.jar"),
    (MODS, "Oh-The-Biomes-Weve-Gone-NeoForge-2.6.0.jar", "https://cdn.modrinth.com/data/NTi7d3Xc/versions/aPEcdSHb/Oh-The-Biomes-Weve-Gone-NeoForge-2.6.0.jar"),
    (MODS, "dungeons-and-taverns-v4.4.4.jar", "https://cdn.modrinth.com/data/tpehi7ww/versions/BYUUUeZA/dungeons-and-taverns-v4.4.4.jar"),
    (MODS, "minecolonies-1.1.1395-1.21.1-snapshot.jar", "https://mediafilez.forgecdn.net/files/8931/927/minecolonies-1.1.1395-1.21.1-snapshot.jar"),
    (MODS, "structurize-1.0.832-1.21.1.jar", "https://mediafilez.forgecdn.net/files/8610/535/structurize-1.0.832-1.21.1.jar"),
    (MODS, "domum-ornamentum-1.0.236-snapshot-main.jar", "https://mediafilez.forgecdn.net/files/8784/713/domum-ornamentum-1.0.236-snapshot-main.jar"),
    (MODS, "multipiston-1.2.58-1.21.1.jar", "https://mediafilez.forgecdn.net/files/7097/877/multipiston-1.2.58-1.21.1.jar"),
    (MODS, "blockui-1.0.205-1.21.1.jar", "https://mediafilez.forgecdn.net/files/6646/615/blockui-1.0.205-1.21.1.jar"),
    (MODS, "stylecolonies-1.15.59-1.21.1.jar", "https://mediafilez.forgecdn.net/files/8782/133/stylecolonies-1.15.59-1.21.1.jar"),
    (MODS, "AmbientSounds_NEOFORGE_v6.3.8_mc1.21.1.jar", "https://cdn.modrinth.com/data/fM515JnW/versions/RZyxhsqY/AmbientSounds_NEOFORGE_v6.3.8_mc1.21.1.jar"),
    (SP, "ComplementaryReimagined_r5.9.3.zip", "https://cdn.modrinth.com/data/HVnmMxH1/versions/Bqen1mJX/ComplementaryReimagined_r5.9.3.zip"),
    (SP, "ComplementaryUnbound_r5.9.3.zip", "https://cdn.modrinth.com/data/R6NEzAwj/versions/B1kyfoUZ/ComplementaryUnbound_r5.9.3.zip"),
    (SP, "Bliss_v2.1.2.zip", "https://cdn.modrinth.com/data/ZvMtQlho/versions/kC2Y8q1P/Bliss_v2.1.2_%28Chocapic13_Shaders_edit%29.zip"),
    (SP, "BSL_v10.1.7.zip", "https://cdn.modrinth.com/data/Q1vvjJYV/versions/sUOU7Iv2/BSL_v10.1.7.zip"),
    (RP, "Excalibur_V26.3.zip", "https://cdn.modrinth.com/data/hJAzl1Bs/versions/PF0DyR5z/Excalibur_V26.3.zip"),
    (RP, "Clarent.zip", "https://cdn.modrinth.com/data/asD9taD4/versions/YSuQQv4R/Clarent_12110_1202%2B_v3.zip"),
    (RP, "FreshAnimations_v1.10.5.zip", "https://cdn.modrinth.com/data/50dA9Sha/versions/RGIzA5em/FreshAnimations_v1.10.5.zip"),
    (RP, "EFA_1.10.5_Hotfix_1.zip", "https://cdn.modrinth.com/data/yiTthr0O/versions/UmkPWet8/EFA_1.10.5%20Hotfix%201.zip"),
    (RP, "Ashen_16x.zip", "https://cdn.modrinth.com/data/LSmohupN/versions/cR2AGjlP/Ashen_16x.zip"),
    (RP, "Demon_slayer.zip", "https://cdn.modrinth.com/data/7QAcy9dW/versions/rmb7beEN/Demon%20slayer.zip"),
]


def download(dest: Path, url: str) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 10000:
        print("  есть ", dest.name)
        return
    print("  качаю", dest.name)
    req = urllib.request.Request(url, headers=UA)
    tmp = dest.with_suffix(dest.suffix + ".part")
    try:
        with urllib.request.urlopen(req, timeout=180) as r, open(tmp, "wb") as f:
            while True:
                chunk = r.read(256 * 1024)
                if not chunk:
                    break
                f.write(chunk)
        tmp.replace(dest)
        print("    ок", dest.stat().st_size, "байт")
    except Exception as e:
        if tmp.exists():
            tmp.unlink()
        print("    ОШИБКА:", dest.name, e)


def main() -> int:
    print("Fantasy Coop installer")
    print("папка:", ROOT)
    ok = 0
    for folder, name, url in FILES:
        download(folder / name, url)
        if (folder / name).exists():
            ok += 1
    print(f"\nГотово: {ok}/{len(FILES)} файлов.")
    print("Скопируйте mods, resourcepacks и shaderpacks в инстанс 1.21.1 NeoForge.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
