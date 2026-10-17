let
    Source = Excel.Workbook(File.Contents("C:\Users\Haris\Documents\ICT_SA_JobMarket_Dataset_v4.xlsx"), null, true),
    JobPostings_Sheet = Source{[Item="JobPostings",Kind="Sheet"]}[Data],
    #"Promoted Headers" = Table.PromoteHeaders(JobPostings_Sheet, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{{"JobID", type text}, {"JobTitle", type text}, {"RoleCategory", type text}, {"JobSector", type text}, {"JobSectorSort", Int64.Type}, {"CareerLevel", type text}, {"CareerLevelSort", Int64.Type}, {"YearsExperienceReq", type text}, {"Employer", type text}, {"Industry", type text}, {"Location", type text}, {"RemoteType", type text}, {"EmploymentType", type text}, {"SalaryMin", Int64.Type}, {"SalaryMax", Int64.Type}, {"SalaryMid", Int64.Type}, {"SalaryBand", type text}, {"QualificationRequested", type text}, {"Source", type text}, {"PostedDate", type date}, {"SkillCount", Int64.Type}, {"SalaryBandSort", Int64.Type}})
in
    #"Changed Type"
