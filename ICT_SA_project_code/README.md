# ICT Job Market Skills Analytics for South Australia: code, in the order it was built

01_data/            The three tables behind the report (JobPostings 400 rows, JobSkills 2,064, Skills 73), read out of the final .pbix.
02_power_query/     Power Query (M) that loads each sheet of ICT_SA_JobMarket_Dataset_v4.xlsx into Power BI.
03_dax/             DAX measures, the MonthStart calculated column, and the model relationships.
04_power_bi_themes/ Colour theme JSON files. v2 failed to import; v2a (colours) and v2b (colours + rounded corners) work. You imported v2b.
05_pbix_tools/      inspect_pbix.py (lists every visual, title, field, slicer sync group and text box in a .pbix) and extract_model.py (pulls DAX, M and tables).
06_web_page/        The web version: template.html + data.json -> build_page.py -> sa_ict_skills_analytics.html (single file, works offline in any browser).
                    shot.js = Playwright test that opens every tab at desktop and phone width and reports errors. Syntax check: extract the page's inline <script> and run `node --check` on it.

Not included: the script that first generated the synthetic dataset and the other early items (Excel workbook builder, Word one-pager, first Chart.js demo).
Those were made in the earlier part of the project and were not saved in this workspace. The data itself is in 01_data.
