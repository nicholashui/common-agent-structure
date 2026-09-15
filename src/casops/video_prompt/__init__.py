"""ISSUE-0009 P1: v2 clip envelope + capability profiles. No live vendor change."""

from casops.video_prompt.assemble import (
    assemble_clip,
    clip_from_projection,
    clip_from_walkthrough,
    project_clip,
    write_clip_files,
)
from casops.video_prompt.compile import (
    compile_clip,
    write_compiled_package,
)
from casops.video_prompt.owners import HEADING_OWNERS, OWNER_PATHS, heading_owner
from casops.video_prompt.patch import (
    OwnershipError,
    apply_choice_overlays,
    apply_owned_patch,
    path_allowed,
)
from casops.video_prompt.profiles import load_profile, load_profiles, profile_for_tag
from casops.video_prompt.schema import (
    CLIP_SCHEMA_ID,
    ClipSchemaError,
    SequenceSchemaError,
    empty_clip,
    empty_sequence,
    validate_clip,
    validate_sequence,
)
from casops.video_prompt.sequence import (
    assemble_sequence,
    compile_sequence,
    sequence_from_clip,
    write_sequence_file,
)

__all__ = [
    "CLIP_SCHEMA_ID",
    "HEADING_OWNERS",
    "OWNER_PATHS",
    "heading_owner",
    "ClipSchemaError",
    "SequenceSchemaError",
    "OwnershipError",
    "apply_choice_overlays",
    "apply_owned_patch",
    "assemble_clip",
    "assemble_sequence",
    "clip_from_projection",
    "clip_from_walkthrough",
    "compile_clip",
    "compile_sequence",
    "empty_clip",
    "empty_sequence",
    "sequence_from_clip",
    "validate_sequence",
    "write_sequence_file",
    "load_profile",
    "load_profiles",
    "path_allowed",
    "profile_for_tag",
    "project_clip",
    "validate_clip",
    "write_clip_files",
    "write_compiled_package",
]
