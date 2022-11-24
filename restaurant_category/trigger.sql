CREATE OR REPLACE FUNCTION DELIVERY_COMPLETE() RETURNS TRIGGER AS
$$
BEGIN
    IF (NEW.TSname = 'Order complete') 
        THEN
        cost := (
        SELECT DeliveryFee 
        FROM TRANSACTION 
        WHERE (Email, Datetime) = (NEW.email, NEW.Datetime)
        );

        UPDATE TRANSACTION_ACTOR 
        SET Restopay = Restopay + cost
        WHERE Email IN (
        SELECT CourierId 
        FROM TRANSACTION
        WHERE (Email, Datetime) = (NEW.Email, NEW.Datetime)
        );

        food_price := (
        SELECT TotalFood 
        FROM TRANSACTION 
        WHERE (Email, Datetime) = (NEW.Email, NEW.Datetime)
        );

        UPDATE TRANSACTION_ACTOR 
        SET Restopay = Restopay + food_price
        WHERE Email = (
        SELECT Email FROM RESTAURANT 
        WHERE (RName, Rbranch) = (
        SELECT Rname, Rbranch 
        FROM TRANSACTION_FOOD 
        WHERE Email = NEW.Email 
        AND Datetime = NEW.Datetime)
        );
    END IF;
    RETURN NEW;
END;
$$
LANGUAGE plpgsql;

CREATE TRIGGER TRIGGER_DELIVERY_COMPLETE
AFTER UPDATE ON TRANSACTION_HISTORY
FOR EACH ROW EXECUTE PROCEDURE DELIVERY_COMPLETE();