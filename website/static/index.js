let roomSelected = -1,
  prevRoom;

function setSelected(roomId) {
  if(roomId == -1)
  {
    window.alert("You have been already alotted a room !!");
    return;
  }
  let room = document.getElementById(roomId.toString());
  console.log(room);
  console.log("roomSelected1 = " + roomSelected);
  if (room.className == "seat occupied") {
    window.alert("This room has already been alotted!! Select another room.");
    return;
  }
  if (prevRoom == room) {
    room.className = "seat";
    prevRoom.className = "seat";
    roomSelected = -1;
    console.log("prev and current room are same- roomSelected2 = " + roomSelected);
    return;
  }
  if (roomSelected != -1) {
    prevRoom.className = "seat";
  }

  if (room.className == "seat selected") {
    room.className = "seat";
    roomSelected = -1;
    prevRoom = None;
  } else if (room.className == "seat") {
    room.className = "seat selected";
    roomSelected = roomId;
  }

  console.log("roomSelected after = " + roomSelected);
  prevRoom = room;
  console.log(prevRoom);
}

function allotRoom(roomId) {
  if(roomSelected==-1)
  {
    window.alert("Please select a room !!");
    return;
  }
  fetch("/allot-room", {
    method: "POST",
    body: JSON.stringify({ roomId: roomSelected }),
  }).then((_res) => {
    window.location.href = "/";
  });
}
