let
    Source = Excel.Workbook(File.Contents("C:\Users\Haris\Documents\ICT_SA_JobMarket_Dataset_v4.xlsx"), null, true),
    JobSkills_Sheet = Source{[Item="JobSkills",Kind="Sheet"]}[Data],
    #"Changed Type" = Table.TransformColumnTypes(JobSkills_Sheet,{{"Column1", type text}, {"Column2", type text}, {"Column3", type text}}),
    #"Promoted Headers" = Table.PromoteHeaders(#"Changed Type", [PromoteAllScalars=true]),
    #"Changed Type1" = Table.TransformColumnTypes(#"Promoted Headers",{{"JobID", type text}, {"SkillName", type text}, {"SkillCategory", type text}})
in
    #"Changed Type1"
