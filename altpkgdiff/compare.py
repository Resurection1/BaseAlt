from collections import defaultdict
from typing import Dict, List
from altpkgdiff.models import Package
from altpkgdiff.rpmver import compare_version_release


def group_by_arch_and_name(packages: List[Package]):
    result = defaultdict(dict)
    for pkg in packages:
        result[pkg.arch][pkg.name] = pkg
    return result


def compare_branches(sisyphus: List[Package], p11: List[Package]) -> Dict:
    sis = group_by_arch_and_name(sisyphus)
    p11g = group_by_arch_and_name(p11)

    result = {}

    for arch in set(sis) | set(p11g):
        sis_pkgs = sis.get(arch, {})
        p11_pkgs = p11g.get(arch, {})

        only_in_sis = sorted(set(sis_pkgs) - set(p11_pkgs))
        only_in_p11 = sorted(set(p11_pkgs) - set(sis_pkgs))

        version_higher = []

        for name in set(sis_pkgs) & set(p11_pkgs):
            sis_vr = sis_pkgs[name].version_release
            p11_vr = p11_pkgs[name].version_release

            if compare_version_release(sis_vr, p11_vr) > 0:
                version_higher.append(
                    {
                        "name": name,
                        "sisyphus": sis_vr,
                        "p11": p11_vr,
                    }
                )

        result[arch] = {
            "only_in_sisyphus": only_in_sis,
            "only_in_p11": only_in_p11,
            "version_higher_in_sisyphus": version_higher,
        }

    return result
