
    set_rating(date, rating:int) → Ratings give evaluative power; essential if you want progress tracking.

    get_summary_for_weekject(date) → Combines weekject, tags, rating = core “view” function.

⚡ Secondary MVP – Should Have (quality of life)

    query_weekjects_from_tag(tag) → Useful inverse lookup (discoverability).

    get_rating(date) → Lets you retrieve ratings (otherwise you can only set blindly).

    delete_tag_from_weekject(date, tag) → Mistakes happen, you need correction.

    

🌱 Nice-to-Have (polish + insights)

    get_top_weekjects_by_rating(n=5) → Encourages reflection.

    get_bottom_weekjects_by_rating(n=5) → Same, but for weak weeks.

    delete_rating(date) → Cleanup, not core.

    delete_weekject(week_no) → Dangerous unless you want destructive editing.

    search_weekjects_by_text(keyword) → Powerful, but not MVP.



🆕 Weekject Core Metrics

    Add new columns to weekject for structured metrics (e.g. mood, productivity, energy, alignment).

    Implement set_metric(date, metric_name, value) → update one metric column.

    Implement get_metric(date, metric_name) → fetch one metric column.

    Implement get_metrics(date) → return all structured metrics for a weekject.

🆕 Custom Tag Groups

    Extend tags table schema to include a tag_group column.

    Implement create_tag_group(group_name) → allows user to define new groups (default = "Custom").

    Implement add_tag_to_group(tag, group) → assigns existing tag to a group.

    Implement query_tags_by_group(group) → list all tags within a group.

    Implement query_weekjects_by_group_value(group, tag_name) → fetch all weekjects tagged with a specific group value (e.g. all “happy” moods).