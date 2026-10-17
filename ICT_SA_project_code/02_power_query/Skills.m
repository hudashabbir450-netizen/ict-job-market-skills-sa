let
    Source = Excel.Workbook(File.Contents("C:\Users\Haris\Documents\ICT_SA_JobMarket_Dataset_v4.xlsx"), null, true),
    Skills_Sheet = Source{[Item="Skills",Kind="Sheet"]}[Data],
    #"Changed Type" = Table.TransformColumnTypes(Skills_Sheet,{{"Column1", type text}, {"Column2", type text}}),
    #"Promoted Headers" = Table.PromoteHeaders(#"Changed Type", [PromoteAllScalars=true]),
    #"Changed Type1" = Table.TransformColumnTypes(#"Promoted Headers",{{"SkillName", type text}, {"SkillCategory", type text}})
in
    #"Changed Type1"
