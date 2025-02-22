SELECT DISTINCT da.acc_id, da.acc_holder
FROM df_accs da
JOIN df_trans dt1 ON da.acc_id = dt1.acc_id
WHERE MONTH(dt1.tran_date) = 4
AND da.acc_id NOT IN (
    SELECT DISTINCT acc_id 
    FROM df_trans 
    WHERE MONTH(tran_date) IN (1, 2, 3)
);
