def menu():
    print("=========================")
    print("\t1.Manage Room Records")
    print("\t2.View System Summary")
    print("\t3.Genrate Performance Report")
    print("\t4.Exit")
    print("=========================")

def room():
    print("=========================")
    print("\t 1.Add Room")
    print("\t 2.Update Room")
    print("\t 3.Delete Room")
    print("\t 4.Exit")
    print("=========================")

while True:
    menu()
    option_menu=input("Please  select only one service(1-4): ")

    while option_menu=="1":
         room() 
         option=input("Please select one service only(choose 1-4): ")

         if option=="1":
            room_ID=input("Enter the Room ID: ")
            room_type=input("Enter the type of room: ")
            Price=input("Enter the price of the room per night: ")
            with open("rooms_record.txt","a") as file:
                file.write(f"Room ID={room_ID}\n")
                file.write(f"Room Type={room_type}\n")
                file.write(f"Price={Price}\n")
                file.write("------------------\n")
    
         elif option=="2":
            roomID=input("Enter the Room ID that you would like to update: ")

            print("Update:")
            print("\t 1.Room Type")
            print("\t 2.Room Price")

            update_option=input("Please select one service only(1-2): ")

            if update_option=="1":
                new_type=input("Enter the updated Room Type: ")
                field="Room Type" 

            elif update_option=="2":
                new_price=input("Enter the updated Room Price: ")
                field="Room Price" 

            else:
                print("Invalid number")
                continue

            with open("rooms_record.txt","r") as file: 
                lists=file.readlines()  

            with open("rooms_record.txt","w") as file: 
                i=0 
                while i<len(lists): 
                    if lists[i].strip()==f"Room ID={roomID}": 
                        file.write(lists[i]) 
                        i=i+1 

                        room_type_lists=lists[i] 
                        room_price_lists=lists[i+1]

                        if field=="Room Type":
                            file.write(f"Room Type={new_type}\n")
                            file.write(room_price_lists) 

                        else:
                            file.write(room_type_lists)
                            file.write(f"Room Price={new_price}\n") 
                        file.write("------------------\n")

                        i+=3

                    else:
                        file.write(lists[i]) 
                        i=i+1
            print("Room succesfully updated!")
    
         elif option=="3":
            roomID=int(input("Enter the Room ID that you would like to delete: "))

            with open("rooms_record.txt","r") as file:
                lists=file.readlines()

            with open("rooms_record.txt", "w") as file:
                i=0
                while i<len(lists):
                    if lists[i].strip()==f"Room ID={roomID}":
                        i=i+4
                        continue

                    file.write(lists[i])
                    i+=1
            print("Room succesfully deleted!")

         elif option=="4":
             break
         
         else:
             print("Invalid number")
             continue
         
    while option_menu=="2":
        print("=========================")
        print("\t1.Total Booking")
        print("\t2.Occupancy Rate")
        print("\t3.Monthly Hotel Income")
        print("\t4.Exit")
        print("=========================")

        option_menu_2=input("Enter one service only(1-4): ")

        if option_menu_2=="1":
            with open ("booking_record.txt","r") as file:
                content=file.read()
                print(content)

        if option_menu_2=="2":
            with open("booking.txt","r") as file:

                count_booked=0

                for row in file:
                    if row.strip():
                        count_booked+=1
                count_booked=count_booked-1
                print(f"Total room has been booked={count_booked}")

            with open("rooms_record.txt","r") as file:

                count_room=0

                for row in file:
                    if row.strip():
                        count_room+=1
                count_room=count_room/4
                print(f"Total room={count_room}")

            occupancy_rate=((count_booked/count_room)*100)
            print(f"The occupancy Rate is={occupancy_rate:.2f}%")

        if option_menu_2=="3":
            total_income=0

            with open("booking.txt","r") as file:
                next(file)
                for row in file:
                    if row.strip():
                        parts=row.strip().split(",")
                        amount=float(parts[-1])
                        total_income+=amount
                print(f"Monthly Hotel Income=Rm{total_income}")

        if option_menu_2=="4":
            break

        else:
            print("Invalid number")
            continue

    while option_menu=="3":
        print("=========================")
        print("\t1.Daily Report")
        print("\t2.Monthly Report")
        print("\t3.Exit")
        print("=========================")

        option_menu_3=input("Please select one service only(1-3): ")

        if option_menu_3=="1":
            date=input("enter the date(YearMonthDay): ")
            check_in=0
            check_out=0
            revenue=0
            total_rooms=0

            with open("booking_record.txt", "r") as file:
                for row in file:
                    row=row.strip()

                    if row==f"Check-in Date={date}":
                        check_in+=1

            with open("booking_record.txt", "r") as file:
                for row in file:
                    row=row.strip()

                    if row==f"Check-out Date={date}":
                        check_out+=1
            print(f"Check-In={check_in}")
            print(f"Check-Out={check_out}")

            with open("booking.txt","r") as file:
                next(file)
                for row in file:
                    if row.strip():
                        parts=row.strip().split(",")
                        if parts[-3]==date:
                            amount=float(parts[-1])
                            revenue=amount+revenue
            print(f"Revenue={revenue}")

            count=0
            with open("rooms_record.txt","r") as file:
                for row in file:
                    row=row.strip()
                    if row=="------------------":
                        count+=1
            total_rooms=count-check_in
            print(f"Total rooms={total_rooms}")
            
        if option_menu_3=="2":
            check_in_month=0
            check_out_month=0
            booked_room_month=0
            monthly_income=0
            total_rooms_month=0
            occupancy_rate_month=0

            with open("booking_record..txt","r") as file:
                for row in file:
                    row=row.strip()
                    if row==f"Status=checked-in":
                        check_in_month+=1
                    if row==f"Status=checked-out":
                        check_out_month+=1
                    if row==f"Status=booked":
                        booked_room_month+=1

            with open("booking.txt","r") as file:
                next(file)
                for row in file:
                    row=row.strip()
                    lines=row.strip().split(",")
                    amount=float(lines[-1])
                    monthly_income+=amount
            
            with open("rooms_record.txt","r") as file:
                for row in file:
                    row=row.strip()
                    if row=="------------------":
                        total_rooms_month+=1

                occupancy_rate_month=((booked_room_month/total_rooms_month)*100)

            print("=========================Monthly Report=========================")
            print(f"Total Check-In={check_in_month}")
            print(f"Total Check-Out={check_out_month}")
            print(f"Total Room Booked={booked_room_month}")
            print("---------------------------------------------------------------")
            print(f"Monthly Income={monthly_income}")
            print("---------------------------------------------------------------")
            print(f"Total Room={total_rooms_month}")
            print(f"Occupancy Rate=({occupancy_rate_month:.2f})%")

        if option_menu_3=="3":
            break

        else:
            print("Invalid number")
            continue

    if option_menu==4:
        print("Thank You for using this system!")
        break

    else:
        print("Invalid number")
        continue